#!/bin/bash
source ../common.ish
 
echo "#############################"
echo "Roles"
echo "#############################"
echo ""

echo "Now we will check out roles..."
echo ""
echo "-----------------------------"

echo "cat site.yml"
cat site.yml
echo ""
echo ""

echo "Testing modules as your are developing"
echo ""
echo ""
cmd="../../ansible/hacking/test-module -m library/hostsfile.py -a 'comment=\"Managed by Ansible\" hostname=\"ansible-test\" ip_address=\"127.0.0.35\" hostfile=\"/tmp/hosts-test\" state=present aliases=test,test2'"
echo "running: $(set_color green "$cmd")"
read -n1 -r -p "Press space to continue..." key
echo ""
echo ""
eval $cmd

cmd="ansible-playbook -i hosts -s site.yml"
echo "running: $(set_color green "$cmd")"
echo ""
read -n1 -r -p "Press space to continue..." key
eval $cmd
