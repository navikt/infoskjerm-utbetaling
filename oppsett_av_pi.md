# Hva må gjøres på Raspberry Pien?

Se full guide i Guide.md

1. Koble til wifi 'infoskjerm'
    - wifi-kortet til Rpien må whitelistes
    - skriv `ifconfig` i terminalen og send det etter "ether" under "wlan0" til Trond Aker (#tech-nettverk)
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
    ... # to linjer som allerede er der

    # skrur av skjermsparer og flytter vekk muspekeren
    @xscreensaver -no-splash
    @xset s off
    @xset -dpms
    @xset s noblank

    # starter bash-script i infoskjerm-karusell etter 5 sekunder pause
    @lxterminal -t temp -e 'sleep 5; ls -a'
    @lxterminal -t karusell_starter -e ~/Desktop/infoskjerm-karusell/karusell.sh
    ````
9. `sudo reboot`


Husk å zoome i nettleseren til passe størrelse. Det blir laget ved reboot.
