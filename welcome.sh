#!/bin/bash
# Script welcome.sh
# 18/09/2023 - Hernan Bocanegra Garcia
#
echo "Hola ${LOGNAME}"
echo "Hoy es $(date)"
echo "Usuarios actuales conectados, y sus procesos:"
w
