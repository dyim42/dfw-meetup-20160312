#!/bin/bash

source "../common.ish"

echo "Ping all hosts"
echo "ansible"
echo "  -i ../hosts <group>   : This is to specify the inventory file that has the hosts"
echo "  <group: all,dev,prod> : see hosts file"
echo "  -m ping               : This is to specify a module to run"
echo "  -u vagrant            : Specify the user we will login as"
echo ""

cmd="ansible -i hosts all -m ping -u vagrant"
echo "running: $(set_color green "$cmd")"
echo ""
echo "-----------------------------"
read -n1 -r -p "Press space to continue..." key
eval $cmd
