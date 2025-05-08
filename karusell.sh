#!/bin/bash
echo "Starter opp karusell for infoskjerm"

# Sjekker om internett er tilgjengelig
while true; do
    if ping -c 1 -q google.com &>/dev/null; then
        echo "Internett er tilgjengelig :party:"
        break
    else
        echo "Ingen internett, prøver igjen om 5 sekunder"
        sleep 5
    fi
done

# Starter infoskjerm-karusell 
sleep 5
lxterminal -t Karusellen -e 'sleep 2; cd ~/Desktop/infoskjerm-karusell; git pull; sleep 2; 
. .venv/bin/activate; python3 infoskjerm_karusell.py; exec bash'