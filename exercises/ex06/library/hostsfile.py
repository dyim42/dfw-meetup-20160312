#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author: David Yim
# Email: dyim42@gmail.com
# Module: Hostsfile
#
# Sample ansible module to demonstrate code structure
#

#----- Documentation Start ------#
DOCUMENTATION = '''
---
version_added: "1.7"
module: hostsfile
short_description: hostsfile
description:
    - This module returns/displays a configured string
options:
    name:
        description:
            Manage hosts file
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

EXAMPLES = '''
- name: Add "ubuntu" to hosts file
  hostsfile: hostname="ubuntu" ip_address="127.0.0.1" state=present

- name: Add "ubuntu" to hosts file
  hostsfile: hostname="ubuntu" ip_address="127.0.0.1" state=absent

- name: Add "ubuntu" to hosts file
  hostsfile: hostname="ubuntu" ip_address="127.0.0.1" state=absent comment="This is a test"

- name: Add "ubuntu" to hosts file
  hostsfile: hostname="ubuntu" ip_address="127.0.0.1" aliases=dev,devlocal  state=present comment="This is a test"
'''

#--- Logic Start -------------------#
import os
import socket

def ip_addr_valid(addr):
    # Checks for valid IPv4 or IPv6 address
    try:
        socket.inet_aton(addr)
    except socket.error:
        try:
            socket.inet_pton(socket.AF_INET6, addr)
        except socket.error:
            return False
    return True


class Hostsfile(object):
    def __init__(self, module, hostfile):
        self.module = module
        self.hostfile = hostfile
        self._raw = None
        self.entries = []
        self.get_host_entries()
        self.added = []
        self.deleted = []

    def get_host_entries(self):
        self.entries = []
        with open(self.hostfile, 'rb') as f:
            self._raw = f.read().strip()

        for line in self._raw.splitlines():
            if line.startswith('#'):
                continue
            if not line:
                continue

            ipaddress, names = line.split(None, 1)
            hostname = names.split()[0]

            comment_start = None
            # Get comment
            if '#' in names:
                # Need to find the index of the # and add everything else after
                # it as a comment
                for n, word in enumerate(names.split()):
                    if word.startswith('#') or '#' in word:
                        comment_start = n + 1
                        break
                comment = ' '.join(names.split()[comment_start:])

            else:
                comment = ''

            # Aliases
            if len(names.split()) > 1:
                aliases = [ali for ali in names.split()[1:comment_start] if not ali.startswith('#')]
            else:
                aliases = []

            self.entries.append({
                'ipaddress': ipaddress,
                'hostname': hostname,
                'aliases': aliases,
                'comment': comment
                })

    def get_entry(self, ipaddress, hostname):
        for entry in self.entries:
            if entry['hostname'] == hostname and \
                    entry['ipaddress'] == ipaddress:
                        return entry
        else:
            return False


    def host_exists(self, ipaddress, hostname):
        if self.get_entry(ipaddress, hostname):
            return True
        else:
            return False

    def add_host(self, ipaddress, hostname, aliases=[], comment=None):
        """
        Add a host to the hosts file
        """
        entry = {
                'ipaddress': ipaddress,
                'hostname': hostname,
                'aliases': aliases,
                'comment': comment
        }
        self.added.append(entry)
        self.entries.append(entry)

    def del_host(self, ipaddress, hostname):
        """
        Add a host to the hosts file
        """
        if self.host_exists(ipaddress=ipaddress, hostname=hostname):
            # delete host
            pass
        else:
            # fail
            pass

        # Find the index of the entry
        index = 0
        for n, entry in enumerate(self.entries):
            if entry['hostname'] == hostname and \
                    entry['ipaddress'] == ipaddress:
                        index = n
        self.entries.pop(index)
        self.deleted.append({'ipaddress': ipaddress, 'hostname': hostname})
        # self.entries.append(entry)

    def _stringify_entries(self):
        output = []
        for entry in self.entries:
            if entry['aliases']:
                aliases = ' '.join(entry['aliases'])
            else:
                aliases = ''

            if entry['comment']:
                comment = '# %s' % entry['comment']
            else:
                comment = ''
            output.append("{}   {} {} {}".format(
                entry['ipaddress'],
                entry['hostname'],
                aliases,
                comment
            ))

        return output

    def update(self):
        output = self._stringify_entries()

        with open(self.hostfile, 'wb') as f:
            f.write("# This file is managed by Ansible!\n")
            f.write("# Do not edit!\n")
            f.write('\n'.join(output))


def main():
    # Note: 'AnsibleModule' is an Ansible utility imported below
    module = AnsibleModule(
            argument_spec=dict(
                    hostfile=dict(required=False, type='str',
                        default='/etc/hosts'),
                    hostname=dict(required=True),
                    ip_address=dict(required=True, type='str'),
                    aliases=dict(required=False, type='list', default=[]),
                    state=dict(choices=['present', 'absent'],
                        default='present'),
                    comment=dict(default=True, type='str'),
            )
            #supports_check_module=True
        )
    hostname = module.params['hostname']
    ip_address = module.params['ip_address']
    aliases = module.params['aliases']
    comment = module.params['comment']

    if not ip_addr_valid(ip_address):
        module.fail_json(msg="Invalid IP Address: %s" % ip_address)

    hosts = Hostsfile(module, module.params['hostfile'])
    changed=False

    new_entry = {
            'ipaddress': ip_address,
            'hostname': hostname,
            'aliases': module.params['aliases'],
            'comment': module.params['comment']
    }

    entry = hosts.get_entry(hostname=hostname, ipaddress=ip_address)
    change = None
    if module.params['state'] == 'present':
        if entry and entry == new_entry:
            changed=False
        else:
            if entry:
                hosts.entries.remove(entry)
            hosts.add_host(**new_entry)
            hosts.update()
            changed=True
            change = hosts.added

    else:
        if hosts.host_exists(hostname=hostname, ipaddress=ip_address):
            hosts.del_host(hostname=hostname, ipaddress=ip_address)
            hosts.update()
            changed=True
            change = hosts.deleted
        else:
            changed=False

    module.exit_json(changed=changed, change=change, entry=entry)

#------- Import Ansible Utilities (Ansible Framework) --------------#
from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()

