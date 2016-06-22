#!/bin/bash
source ../common.ish
 
echo "#############################"
echo "Roles"
echo "#############################"
echo ""

echo "Now we will check out Ansible's Galaxy..."
echo ""
echo "-----------------------------"
read -n1 -r -p "Press space to continue..." key
echo ""

cmd="ansible-galaxy --help"
echo "running: $(set_color green "$cmd")"
echo ""
echo "-----------------------------"
read -n1 -r -p "Press space to continue..." key
eval $cmd
echo ""

cmd="ansible-galaxy search tmux"
echo "running: $(set_color green "$cmd")"
echo ""
echo "-----------------------------"
read -n1 -r -p "Press space to continue..." key
eval $cmd
echo ""

cmd="ansible-galaxy install kbrebanov.tmux -p ./roles/"
echo "running: $(set_color green "$cmd")"
echo ""
echo "-----------------------------"
read -n1 -r -p "Press space to continue..." key
eval $cmd
echo ""

cmd="cat site.yml"
echo "running: $(set_color green "$cmd")"
echo ""
echo "-----------------------------"
read -n1 -r -p "Press space to continue..." key
eval $cmd
echo ""

cmd="ansible-playbook -i hosts -s site.yml"
echo "running: $(set_color green "$cmd")"
echo ""
echo "-----------------------------"
read -n1 -r -p "Press space to continue..." key
eval $cmd
echo ""


