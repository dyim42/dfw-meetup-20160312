#!/bin/bash

echo "running commands with Ansible"
echo "ansible"
echo "  -i ../hosts <group>   : This is to specify the inventory file that has the hosts"
echo "  <group: all,dev,prod> : see hosts file"
echo "  -a command            : This is to specify a module to run"
echo "  -s                    : Use sudo"
echo "  -u vagrant            : Specify the user we will login as"
echo ""

cmd="ansible -i hosts all -s -u vagrant -a 'apt-get install tmux -y'"
echo "running: $cmd"
echo ""
eval $cmd
