#!/bin/bash
echo "Refresherl for tabs"

sleep 5
lxterminal -t refresher -e 'sleep 2; cd /home/pi/Desktop/infoskjerm; git pull; sleep 2; . .venv/bin/activate; python3 infoskjerm_browser.py; exec bash'
