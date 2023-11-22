#!/bin/bash
# Script superscan.sh
# 18/09/2023 - Hernan Bocanegra Garcia
#
# Ejemplo de Menu en BASH
#
date
    echo "||"
    echo "||===========================||"
    echo "||   Menu Principal          ||"
    echo "||===========================||"
    echo "||I. Net Discover"
    echo "||II. Portscanv1"
    echo "||III. Welcome"
    echo "||IV. Exit"
    echo "||"
read -p "Opción  [ 1 - 4 ] " c
case $c in
        1) $HOME/Desktop/netdiscover.sh;;
        2) $HOME/Desktop/portscanv1.sh;;
        3) $HOME/Desktop/welcome.sh;;
        4) echo "Bye!"; exit 0;;
esac
