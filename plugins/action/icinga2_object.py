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
		object_type = args.pop('type', None)
		extra_keywords = dict()
		extra_keywords["host"] = [
		  "address",
		  "address6",
		  "display_name",
		  "groups",
	  	"check_command",
	  	"max_check_attempts",
	  	"check_period",
	  	"check_timeout",
	  	"check_interval",
	  	"retry_interval",
	  	"enable_notifications",
	   	"enable_active_checks",
	  	"enable_passive_checks",
	  	"enable_event_handler",
	  	"enable_flapping",
  		"enable_perfdata",
   		"event_command",
  		"flapping_threshold_high",
	  	"flapping_threshold_low",
	  	"volatile",
	  	"zone",
	  	"command_endpoint",
	  	"notes",
	  	"notes_url",
  		"action_url",
	  	"icon_image",
	  	"icon_image_alt",
			"vars"
		]
		extra_keywords["hostgroup"] = [
		  "display_name",
		  "groups",
		]
		extra_keywords["apiuser"] = [
		  "password",
			"permissions",
			"client_cn"
		]
		extra_keywords["apilistener"] = [
		  "ticket_salt",
			"bind_host",
			"bind_port",
			"accept_config",
			"accept_commands",
			"max_anonymous_clients",
			"cipher_list",
			"tls_protocolmin",
			"tls_handshake_timeout",
			"access_control_allow_origin",
			"environment"
		]
		extra_keywords["checkcommand"] = [
		  "command",
			"env",
			"timeout",
			"arguments",
			"vars"
		]
		extra_keywords["idomysqlconnection"] = [
		  "host",
		  "port",
		  "socket_path",
		  "user",
		  "password",
		  "database",
		  "enable_ssl",
		  "ssl_key",
		  "ssl_cert",
		  "ssl_ca",
		  "ssl_capath",
		 	"ssl_cipher",
		  "table_prefix",
		  "instance_name",
		  "instance_description",
		  "enable_ha",
		  "failover_timeout",
		  "cleanup",
		  "categories"
		]
		extra_keywords["idopgsqlconnection"] = [
		  "host",
		  "port",
	    "user",
		  "password",
		  "database",
		  "ssl_mode",
		  "ssl_key",
			"ssl_cert",
			"ssl_ca",
			"table_prefix",
			"instance_name",
			"instance_description",
			"enable_ha",
			"failover_timeout",
			"cleanup",
			"categories"
		]
		extra_keywords["checkercomponent"] = []
		extra_keywords["endpoint"] = [
		  "host",
			"port",
			"log_duration"
		]
		extra_keywords["filelogger"] = [
		  "path",
			"severity",
		]
		extra_keywords["graphitewriter"] = [
		  "host",
			"port",
			"host_name_template",
			"service_name_template",
			"enable_send_thresholds",
			"enable_send_metadata",
			"enable_ha"
		]
		extra_keywords["icingaapplication"] = [
		  "enable_notifications",
			"enable_event_handlers",
			"enable_flapping",
			"enable_host_checks",
			"enable_service_checks",
			"enable_perfdata",
			"environment",
			"vars"
		]
		extra_keywords["influxdbwriter"] = [
		  "host",
			"port",
			"database",
			"username",
			"password",
			"ssl_enable",
			"ssl_ca_cert",
			"ssl_cert",
			"ssl_key",
			"host_template",
			"service_template",
			"enable_send_thresholds",
			"enable_send_metadata",
			"flush_interval",
			"flush_threshold",
			"enable_ha"
		]
		extra_keywords["notificationcomponent"] = [
		  "enable_ha"
		]
		extra_keywords["service"] = [
		  "display_name",
			"host_name",
			"groups",
			"check_command",
			"max_check_attempts",
			"check_period",
			"check_timeout",
			"check_interval",
			"retry_interval",
			"enable_notification",
			"enable_active_checks",
			"enable_passive_checks",
			"enable_event_handler",
			"enable_flapping",
			"flapping_threshold_high",
			"flapping_threshold_low",
			"enable_perfdata",
			"event_command",
			"volatile",
			"zone",
			"command_endpoint",
			"notes",
			"notes_url",
			"icon_image",
			"icon_image_alt"
		]
		extra_keywords["servicegroup"] = [
		  "display_name",
			"groups"
		]
		extra_keywords["sysloglogger"] = [
		  "severity",
			"facility"
		]
		extra_keywords["timeperiod"] = [
		  "display_name",
			"ranges",
			"prefer_includes",
			"excludes",
			"includes"
		]
		extra_keywords["zone"] = [
		  "endpoints",
			"parent",
			"global"
		]

		if object_type not in task_vars['icinga2_object_types']:
			raise AnsibleError('unknown Icinga object type: %s' % object_type)

		#
		# distribute to object type as module (name: icinga2_type)
		#
		obj = dict()
		obj = self._execute_module(module_name='icinga2_'+object_type.lower(), module_args=args, task_vars=task_vars, tmp=tmp)

		if 'failed' in obj:
			raise AnsibleError('%s' % obj['msg'])

		#
		# file path handling for assemble
		#
		path = task_vars['icinga2_fragments_path'] + '/' + obj['file'] + '/'
		file_fragment = path + obj['order'] + '_' + object_type.lower() + '-' + obj['name']

		file_args = dict()
		file_args['state'] = 'directory'
		file_args['path'] = path
		file_module = self._execute_module(module_name='file', module_args=file_args, task_vars=task_vars, tmp=tmp)
		result = merge_hash(result, file_module)

		if obj['state'] != 'absent':
			varlist = list() # list of variables from 'apply for'

			#
			# quoting of object name?
			#
			if obj['name'] not in task_vars['icinga2_combined_constants']:
				object_name = '"' + obj['name'] + '"'
			else:
				object_name = obj['name']

			#
			# apply rule?
			#
			if 'apply' in obj and obj['apply']:
				object_content = 'apply ' + object_type
				if 'apply_for' in obj and obj['apply_for']:
					object_content += ' for (' + obj['apply_for'] + ') '
					if (r := re.search(r'^(.+)\s+in\s+', obj['apply_for'])):
        					tmp = r.group(1).strip()
        					if (r := re.search(r'^(.+)=>(.+)$', tmp)):
                					varlist.extend([r.group(1).strip(), r.group(2).strip()])
        					else:
                					varlist.append(tmp)
				else:
					object_content += ' ' + object_name
			#
			# template?
			#
			elif 'template' in obj and obj['template']:
				object_content = 'template ' + object_type + ' ' + object_name
			#
			# object
			#
			else:
				object_content = 'object ' + object_type + ' ' + object_name
			object_content += ' {\n'

			#
			# imports?
			#
			if 'imports' in obj:
				for item in obj['imports']:
					object_content += '  import "' + str(item) + '"\n'
				object_content += '\n'

			#
			# parser
			#
			object_content += Icinga2Parser().parse(obj["args"], list(task_vars['icinga2_combined_constants'].keys())+task_vars['icinga2_reserved']+varlist+extra_keywords[object_type.lower()], 2) + '}\n'
			copy_action = self._task.copy()
			copy_action.args = dict()
			copy_action.args['dest'] = file_fragment
			copy_action.args['content'] = object_content

			copy_action = self._shared_loader_obj.action_loader.get('copy',
				task=copy_action,
				connection=self._connection,
				play_context=self._play_context,
				loader=self._loader,
				templar=self._templar,
				shared_loader_obj=self._shared_loader_obj)

			result = merge_hash(result, copy_action.run(task_vars=task_vars))
		else:
			# remove file if does not belong to a feature
			if 'features-available' not in path:
				file_args = dict()
				file_args['state'] = 'absent'
				file_args['path'] = file_fragment
				file_module = self._execute_module(module_name='file', module_args=file_args, task_vars=task_vars, tmp=tmp)
				result = merge_hash(result, file_module)
			result['dest'] = file_fragment

		return result
