#!/bin/bash
source ../common.ish
 
echo "#############################"
echo "Roles"
echo "#############################"
echo ""

echo "Now we will check out roles..."
echo "-----------------------------"
read -n1 -r -p "Press space to continue..." key
echo ""

echo "cat site.yml"
cat site.yml
echo ""
echo "-----------------------------"
read -n1 -r -p "Press space to continue..." key
echo ""

cmd="ansible-playbook -i hosts -s site.yml"
echo "running: $(set_color green "$cmd")"
echo ""
echo "-----------------------------"
read -n1 -r -p "Press space to continue..." key
eval $cmd
