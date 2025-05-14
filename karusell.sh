#!/bin/bash
LOG_FILE=~/Desktop/infoskjerm-karusell/karusell.log

# Starter logging
echo "" | tee -a "$LOG_FILE"
echo "$(date +%Y-%m-%d_%H:%M:%S) - Starter opp karusell for infoskjerm" | tee -a "$LOG_FILE"

# Sjekker om internett er tilgjengelig
while true; do
    if ping -c 1 -q google.com &>/dev/null; then
        echo "Internett er tilgjengelig :party:" | tee -a "$LOG_FILE"
        break
    else
        echo "Ingen internett, prøver igjen om 20 sekunder" | tee -a "$LOG_FILE"
        sleep 20
    fi
done

# Starter infoskjerm-karusell
sleep 5
lxterminal -t Karusellen -e 'sleep 2; cd ~/Desktop/infoskjerm-karusell; git pull; sleep 2; 
. .venv/bin/activate; python3 infoskjerm_karusell.py; exec bash' >> "$LOG_FILE" 2>&1