# Hva må gjøres på Raspberry Pien?

Se full guide i Guide.md

1. Koble til wifi 'infoskjerm'
2. Logg inn på AD-brukeren 'srvdevinfoskjerm111@nav.no'
    - Passord for wifi og sørvisbruker i GSM
    - Logg feks inn på: https://data.ansatt.nav.no/quarto/0b700511-f50c-4059-b519-32fb19637bae
2. `sudo apt-get install xscreensaver`
3. `sudo raspi-config` og skru av "screen blanking" under "display settings"
4. `git clone http://github.com/navikt/infoskjerm-karusell.git`
5. `cd infoskjerm-karusell`
6. `chmod +x karusell.sh`
7. `python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt`
8. `sudo nano /etc/xdg/lxsession/LXDE-pi/autostart` og legg til følgende linjer:
    
    ````bash
    @xscreensaver -no-splash # usikker på denne

    # skrur av skjermsparer og flytter vekk muspekeren
    @xset s off
    @xset -dpms
    @xset s noblank

    # starter bash-script i infoskjerm-karusell
    @lxterminal -t lxterm -e /home/pi/Desktop/infoskjerm-karusell/karusell.sh
    ````
9. `sudo reboot`