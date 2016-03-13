#!/usr/bin/python

from ansible.module_utils.basic import *

module = AnsibleModule(
    argument_spec = dict(
        state     = dict(default='present', choices=['present', 'absent']),
        name      = dict(required=True),
        enabled   = dict(required=True, type='bool'),
        something = dict(aliases=['whatever'])
    ),
    # supports_check_mode=True
)

# if module.check_mode:
#     # Check if any changes would be made but don't actually make those changes
module.exit_json(changed=True, something_else=12345)
module.fail_json(msg="Something fatal happened")

if __name__ == '__main__':
    main()
