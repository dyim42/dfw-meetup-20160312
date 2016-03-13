#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author: David Yim
# Email: dyim42@gmail.com
#
# Sample ansible module to demonstrate code structure
#

#----- Documentation Start ------#
DOCUMENTATION = '''
---
version_added: "1.7"
module: echo
short_description: echo
description:
    - This module returns/displays a configured string
options:
    name:
        description:
            text message to print
    success:
        description:
            If false, the module will exit with failure
        required: false
        default: yes
        choices: [ "yes", "no" ]
notes:
    - This module does not connect to host. It is a dummy module
      required: true
requirements: []
author: David Yim
'''
#--- Logic Start -------------------#

def main():
    # Note: 'AnsibleModule' is an Ansible utility imported below
    module = AnsibleModule(
            argument_spec=dict(
                    name=dict(required=True),
                    success=dict(default=True, type='bool'),
            )
            #supports_check_module=True
        )
    success = module.params['success']
    text = module.params['name']
    if success:
        module.exit_json(text=text)
    else:
        module.fail_json(msg=text)

#------- Import Ansible Utilities (Ansible Framework)
from ansible.module_utils.basic import *
main()

# Examples:
# - echo: name="Hello World!"
# - echo: name="Success is yes" success=yes
# - echo: name="Success is no" success=no
