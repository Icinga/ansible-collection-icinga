# pylint: disable=consider-using-f-string,super-with-arguments
import re

from ansible.plugins.action import ActionBase
from ansible.utils.vars import merge_hash
from ansible_collections.icinga.icinga.plugins.module_utils.parse import Icinga2Parser


class ActionModule(ActionBase):

    def __init__(self, *args, **kwargs):
        super(ActionModule, self).__init__(*args, **kwargs)
        self.combined_constants_keys = None
        self.icinga2_reserved = None
        self.ensured_directories = set()

    def run(self, tmp=None, task_vars=None):
        result = super(ActionModule, self).run(tmp, task_vars)

        # Check if 'objects' parameter is provided
        if 'objects' in self._task.args:
            # Process multiple objects
            objects = self._task.args.get('objects', [])
            if not objects:
                return result  # No objects to process

            # Initialize overall result
            aggregate_result = {
                'changed': False,
                'results': [],
                'dest': [],
                'failed': False,
            }

            # Cache constants and reserved words as instance variables
            self.combined_constants_keys = list(task_vars['icinga2_combined_constants'].keys())
            self.icinga2_reserved = task_vars['icinga2_reserved']

            # Keep track of directories we've already ensured
            self.ensured_directories = set()

            # Process each object
            for item in objects:
                obj_result = self.process_object(item, tmp, task_vars)
                if obj_result.get('failed'):
                    aggregate_result['failed'] = True
                    aggregate_result['msg'] = obj_result['msg']
                    return aggregate_result

                aggregate_result['results'].append(obj_result)
                aggregate_result['dest'].append(obj_result['dest'])
                if obj_result.get('changed'):
                    aggregate_result['changed'] = True

            # If only one object, flatten the result for backward compatibility
            if len(aggregate_result['results']) == 1:
                single_result = aggregate_result['results'][0]
                aggregate_result.update(single_result)
                # Remove 'results' and 'dest' list to match original structure
                aggregate_result.pop('results', None)
                aggregate_result['dest'] = single_result['dest']
            else:
                # Keep 'dest' as a list if multiple objects
                pass

            return aggregate_result

        # Process a single object using individual arguments
        args = self._task.args.copy()

        # Cache constants and reserved words as instance variables
        self.combined_constants_keys = list(task_vars['icinga2_combined_constants'].keys())
        self.icinga2_reserved = task_vars['icinga2_reserved']
        self.ensured_directories = set()

        result = self.process_object(args, tmp, task_vars)
        return result

    def process_object(self, args, tmp, task_vars):
        # Merge args
        args = args.copy()
        object_args = args.pop('args', {})
        args = merge_hash(object_args, args)
        object_type = args.pop('type', None)

        if object_type not in task_vars['icinga2_object_types']:
            return {'failed': True, 'msg': 'Unknown Icinga object type: %s' % object_type}

        # Execute the module for the object type
        obj = self._execute_module(
            module_name='icinga2_' + object_type.lower(),
            module_args=args,
            task_vars=task_vars,
            tmp=tmp
        )

        if obj.get('failed'):
            return {'failed': True, 'msg': 'Call to module failed: %s' % obj['msg']}
        if obj.get('skipped'):
            return {'failed': True, 'msg': 'Call to module was skipped: %s' % obj['msg']}

        # File path handling for assemble
        path = task_vars['icinga2_fragments_path'] + '/' + obj['file'] + '/'
        file_fragment = path + obj['order'] + '_' + object_type.lower() + '-' + obj['name']

        # Initialize the result for this object
        obj_result = {
            'changed': False,
            'dest': file_fragment,
            'state': obj['state'],
            'name': obj['name'],
            'type': object_type,
        }

        if obj['state'] != 'absent':
            varlist = []  # List of variables from 'apply for'

            # Quoting of object name?
            if obj['name'] not in task_vars['icinga2_combined_constants']:
                object_name = '"' + obj['name'] + '"'
            else:
                object_name = obj['name']

            # Apply rule?
            if obj.get('apply'):
                if not obj['args'].get('assign'):
                    return {'failed': True, 'msg': 'Apply rule %s is missing the assign rule.' % obj['name']}
                object_content = 'apply ' + object_type
                if obj.get('apply_target'):
                    object_content += ' ' + object_name + ' to ' + obj['apply_target']
                elif obj.get('apply_for'):
                    object_content += ' for (' + obj['apply_for'] + ') '
                    r = re.search(r'^(.+)\s+in\s+', obj['apply_for'])
                    if r:
                        tmp_var = r.group(1).strip()
                        r2 = re.search(r'^(.+)=>(.+)$', tmp_var)
                        if r2:
                            varlist.extend([r2.group(1).strip(), r2.group(2).strip()])
                        else:
                            varlist.append(tmp_var)
                else:
                    object_content += ' ' + object_name
            # Template?
            elif obj.get('template'):
                object_content = 'template ' + object_type + ' ' + object_name
            # Object
            else:
                object_content = 'object ' + object_type + ' ' + object_name

            object_content += ' {\n'

            # Imports?
            if obj.get('imports'):
                for item_import in obj['imports']:
                    if item_import.startswith('host.vars'):
                        object_content += '  import ' + str(item_import) + '\n'
                    else:
                        object_content += '  import "' + str(item_import) + '"\n'
                object_content += '\n'

            # Prepare keys for parsing
            all_keys = self.combined_constants_keys + self.icinga2_reserved + varlist + list(obj['args'].keys())
            parsed_content = Icinga2Parser().parse(obj['args'], all_keys, 2)
            object_content += parsed_content + '}\n'

            # Ensure directory exists (optimize by checking if already ensured)
            if path not in self.ensured_directories:
                file_args = {
                    'state': 'directory',
                    'path': path
                }

                file_module = self._execute_module(
                    module_name='file',
                    module_args=file_args,
                    task_vars=task_vars,
                    tmp=tmp
                )

                if file_module.get('changed', False):
                    obj_result['changed'] = True

                # Add to ensured directories
                self.ensured_directories.add(path)

            # Write the object content to the file
            copy_args = {
                'dest': file_fragment,
                'content': object_content
            }

            copy_module = self._execute_module(
                module_name='copy',
                module_args=copy_args,
                task_vars=task_vars,
                tmp=tmp
            )

            if copy_module.get('changed', False):
                obj_result['changed'] = True

        else:
            # Remove file if it does not belong to a feature
            if 'features-available' not in path:
                file_args = {
                    'state': 'absent',
                    'path': file_fragment
                }
                file_module = self._execute_module(
                    module_name='file',
                    module_args=file_args,
                    task_vars=task_vars,
                    tmp=tmp
                )
                if file_module.get('changed', False):
                    obj_result['changed'] = True

        return obj_result
