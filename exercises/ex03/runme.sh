#!/bin/bash
 

echo "executing first ansible run"
echo "ansible-playbook"
echo "  -i ../hosts <group>   : This is to specify the inventory file that has the hosts"
echo "  <group: all,dev,prod> : see hosts file"
echo "  -a command            : This is to specify a module to run"
echo "  -s                    : Specify the site.yml"
echo ""

echo "The contents of the simple.yml file"
cat simple.yml
read -n1 -r -p "Press space to continue..." key
echo ""

cmd="ansible-playbook -i hosts -s simple.yml"
echo "running: $cmd"
echo ""
eval $cmd

echo ""


echo "The contents of the with_handlers.yml file"
cat with_handlers.yml
echo ""
read -n1 -r -p "Press space to continue..." key
echo ""

cmd="ansible-playbook -i hosts -s with_handlers.yml"
echo "running: $cmd"
echo ""
eval $cmd


echo "The contents of the nginx.yml file"
cat nginx.yml
echo ""
read -n1 -r -p "Press space to continue..." key

echo ""

cmd="ansible-playbook -i hosts -s nginx.yml"
echo "running: $cmd"
echo ""
eval $cmd
