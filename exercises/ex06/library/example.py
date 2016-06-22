#!/usr/bin/python

from ansible.constants import mk_boolean
from ansible.module_utils.basic import *

# getters and setters
def _set_value(module, key, value, argument_type, additional_args):
    '''Set value of setting, under `key`, using gconftool-2 to `value`
    of type `argument_type`'''
    cmd = '/usr/bin/gconftool-2 --set --type {} {} "{}" {}'
    return module.run_command(" ".join([cmd.format(argument_type,
        key, value, additional_args)]))

def _get_value(module, key):
    '''Return value of setting, under `key`, from gconftool-2'''
    return module.run_command('gconftool-2 --get {}'.format(key))[1].strip()

def main():
    # module specification
    module = AnsibleModule(
        argument_spec={
            'key': {'required': True},
            'bool': {'type': 'bool'},
            'int': {'type': 'int'},
            'string': {'type': 'str'},
            'float': {'type': 'float'},
            'list': {'type': 'list'},
            'pair': {'type': 'list'},
            'pair-cdr-type': {'choices': ['int', 'bool', 'float', 'string']},
            'pair-car-type': {'choices': ['int', 'bool', 'float', 'string']},
            'list-type': {'choices': ['int', 'bool', 'float', 'string']}
        },
        mutually_exclusive=[
            ['bool', 'string', 'int', 'float', 'list', 'pair'],
            ['bool', 'string', 'int', 'float', 'list-type', 'pair'],
            ['bool', 'string', 'int', 'float', 'list', 'pair-car-type'],
            ['bool', 'string', 'int', 'float', 'list', 'pair-cdr-type'],
        ],
        required_one_of=[['bool', 'string', 'int', 'float', 'list', 'pair']],
        required_together=[
            ['pair', 'pair-car-type', 'pair-cdr-type'],
            ['list', 'list-type']
        ],
        supports_check_mode=True
    )

    key = module.params['key']
    boolean_value = module.params['bool']
    string_value = module.params['string']
    integer_value = module.params['int']
    float_value = module.params['float']
    list_value = module.params['list']
    pair_value = module.params['pair']

    additional_args = ''
    instance_type_mapping = {'int': int, 'string': str, 'float': float, 'bool':
            mk_boolean}

    if boolean_value is not None:
        argument_type = 'bool'
        value = str(mk_boolean(boolean_value)).lower()
        old_value = str(mk_boolean(old_value)).lower()
        #...
    elif float_value is not None:
        argument_type = 'float'
        value = float_value
        # ...
    elif pair_value is not None:
        if len(pair_value) != 2:
            module.fail_json(msg='A pair must be a list of length 2, {} items
                    found.'.format(len))
        argument_type = 'pair'
        try:
            car_value = pair_value[0]
            car_type = module.params['pair-car-type']
            if car_type == 'bool':
                module.boolean(car_value)
                car_value = mk_boolean(car_value)
            elif not str(instance_type_mapping)


    old_value = _get_value(module, key)
    # argument parsing

    changed = old_value != str(value)

    if changed and not module.check_mode:
        _set_value(module, key, value, argument_type, additional_args)

    module.exit_json(
        changed=changed,
        key=key,
        type=argument_type,
        value=value,
        old_value=old_value
    )

if __name__ == '__main__':
    main()
