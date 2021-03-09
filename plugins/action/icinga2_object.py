import re

from ansible.errors import AnsibleError, AnsibleFileNotFound
from ansible.plugins.action import ActionBase
from ansible.module_utils._text import to_native
from ansible.utils.vars import merge_hash
from ansible_collections.icinga.icinga.plugins.module_utils.parse import Icinga2Parser

class ActionModule(ActionBase):

	def run(self, tmp=None, task_vars=None):

		result = super(ActionModule, self).run(tmp, task_vars)

		args = dict()
		args = self._task.args.copy()
		args = merge_hash(args.pop('args', {}), args)
		type = args.pop('type', None)

		if type not in task_vars['icinga2_object_types']:
			raise AnsibleError('unknown Icinga object type: %s' % type)

		obj = dict()
		obj = self._execute_module(module_name='icinga2_'+type.lower(), module_args=args, task_vars=task_vars, tmp=tmp)

		if 'failed' in obj:
			raise AnsibleError('%s' % obj['msg'])

		#
		# file path handling
		#
		path = task_vars['icinga2_fragments_path'] + '/' + obj['file'] + '/'
		file_fragment = path + obj['order'] + '_' + type.lower() + '-' + obj['name']

		file_args = dict()
		file_args['state'] = 'directory'
		file_args['path'] = path
		test = self._execute_module(module_name='file', module_args=file_args, task_vars=task_vars, tmp=tmp)

		
		res = dict()
		res = merge_hash(result, test)

		if obj['state'] != 'absent':
			common_args = dict()
			common_args['content'] = 'object ' + type + ' '

			if obj['name'] not in task_vars['icinga2_combined_constants']:
				common_args['content'] += '"' + obj['name'] + '" {\n'
			else:
				common_args['content'] += obj['name'] + ' {\n'

			common_args['dest'] = file_fragment
			common_args['content'] += Icinga2Parser().parse(obj["args"], list(task_vars['icinga2_combined_constants'].keys())+task_vars['icinga2_reserved'], 2) + '}\n'

			copy_action = self._task.copy()
			copy_action.args = common_args

			copy_action = self._shared_loader_obj.action_loader.get('copy',
				task=copy_action,
				connection=self._connection,
				play_context=self._play_context,
				loader=self._loader,
				templar=self._templar,
				shared_loader_obj=self._shared_loader_obj)

			res = merge_hash(res, copy_action.run(task_vars=task_vars))
		else:
			if 'features-available' not in path:
				copy_args = dict()
				copy_args['state'] = 'absent'
				copy_args['path'] = file_fragment
				test = self._execute_module(module_name='file', module_args=copy_args, task_vars=task_vars, tmp=tmp)
				res = merge_hash(res, test)
			res['dest'] = file_fragment

		return res

