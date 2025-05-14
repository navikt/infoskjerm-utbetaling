# Hva må gjøres på Raspberry Pien?

Se full guide i Guide.md

1. Koble til wifi 'infoskjerm'
    - wifi-kortet til Rpien må whitelistes
    - skriv `ifconfig` i terminalen og send det etter "ether" under "wlan0" til Trond Aker (#tech-nettverk)
1. Pass på at RPIen bruker X11 og ikke Wayland
    - `sudo raspi-config` og velg "Advanced Options" -> "Wayland" -> velg X11, så reboot
2. `sudo apt-get install xscreensaver`
3. `sudo raspi-config` og skru av "screen blanking" under "display settings"
2. Logg inn på AD-brukeren 'srvdevinfoskjerm111@nav.no'
    - Passord for wifi og sørvisbruker i GSM
    - Logg feks inn på: https://data.ansatt.nav.no/quarto/0b700511-f50c-4059-b519-32fb19637bae
4. `git clone http://github.com/navikt/infoskjerm-karusell.git`
5. `cd infoskjerm-karusell` og `cp .bash_aliases ~/.bash_aliases`
6. Tillat kjøring av bash-script`chmod +x karusell.sh`
7. Lag et .venv og installer avhengigheter (autopygui). Bruk feks `mkvenv`
8. `sudo nano /etc/xdg/lxsession/LXDE-pi/autostart` og legg til følgende linjer:
    ````bash
    ... # to linjer som allerede er der

    # skrur av skjermsparer og flytter vekk muspekeren
    @xscreensaver -no-splash
    @xset s off
    @xset -dpms
    @xset s noblank

    # starter bash-script i infoskjerm-karusell etter 5 sekunder pause
    @lxterminal -t tidsbuffer -e 'sleep 5; echo "Done" && exit'
    @lxterminal -t karusellen -e ~/Desktop/infoskjerm-karusell/karusell.sh
    ````
9. `sudo reboot`
10. Sett opp daglig reboot av RPIen, med logg av rebooten:
    - `sudo crontab -e` og legg til linjen:
    ```
    0 6 * * * sudo reboot && echo "$(date) - Systemet startet på nytt av cron" >> ~/Desktop/infoskjerm-karusell/karusell.log
    ```

Husk å zoome i nettleseren til passe størrelse. Det blir laget ved reboot.


Gammel guide med mer tekst tilgjenglig i canvaset i kanalen `#infoskjerm` på slack
