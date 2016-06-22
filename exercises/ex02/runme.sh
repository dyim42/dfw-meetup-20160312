#!/bin/bash
source "../common.ish"

echo "running commands with Ansible"
echo "ansible"
echo "  -i ../hosts <group>   : This is to specify the inventory file that has the hosts"
echo "  <group: all,dev,prod> : see hosts file"
echo "  -a command            : This is to specify a module to run"
echo "  -s                    : Use sudo"
echo "  -u vagrant            : Specify the user we will login as"
echo ""

cmd="ansible -i hosts all -s -u vagrant -a 'apt-get install tmux -y'"
echo "running: $(set_color green "$cmd")"
echo ""
echo "-----------------------------"
read -n1 -r -p "Press space to continue..." key
eval $cmd

echo ""
echo ""


echo "This is for idompotency. Only do something if it doesn't match the expected state"
cmd="ansible -i hosts all -s -u vagrant -m apt -a 'pkg=tmux state=installed update_cache=true'"
echo "running: $(set_color green "$cmd")"
echo ""
echo "-----------------------------"
read -n1 -r -p "Press space to continue..." key
eval $cmd

