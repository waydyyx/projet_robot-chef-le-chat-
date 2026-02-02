#! /bin/bash

[ $# -ne 5 ] && echo "Veuillez enter 5 arguments, vitesse ([int] 0-10), vitesse_rotation ([int] 0-10), l'angle ([int] 0-359), position x ([int]), position y ([int])" && exit 1
cd sources
python3 main.py $1 $2 $3 $4 $5
cd ..
