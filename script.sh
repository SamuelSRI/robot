#!/bin/bash

# Fonction pour lancer une commande dans un nouveau terminal gnome-terminal
function run_in_terminal() {
    gnome-terminal -- bash -c "$1; exec bash"
}

# Commande pour sourcer le fichier install/setup.bash
run_in_terminal "source install/setup.bash"

# Commande pour lancer le fichier rsp.launch.py avec ros2 launch
run_in_terminal "ros2 launch mapping rsp.launch.py"

# Commande pour exécuter joint_state_publisher_gui avec ros2 run
run_in_terminal "ros2 run joint_state_publisher_gui joint_state_publisher_gui"

# Commande pour lancer rviz2
run_in_terminal "rviz2"
