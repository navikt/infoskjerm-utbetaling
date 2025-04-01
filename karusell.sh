#!/bin/bash
echo "Karusell for infoskjerm"

sleep 5
lxterminal -t karusell -e 'sleep 2; cd /home/pi/Desktop/infoskjerm-karusell; git pull; sleep 2; 
. .venv/bin/activate; python3 infoskjerm_karusell.py; exec bash'
