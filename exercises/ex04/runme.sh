#!/bin/bash
 
echo "#############################"
echo "Roles"
echo "#############################"
echo ""

echo "Now we will check out roles..."
echo ""
echo "-----------------------------"

echo "cat dev.yml"
cat dev.yml
echo ""
read -n1 -r -p "Press space to continue..." key

echo ""

cmd="ansible-playbook -i hosts -s dev.yml"
echo "running: $cmd"
echo ""
eval $cmd
