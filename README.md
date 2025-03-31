Filer til infoskjermen på kontoret


## Hva er greia?

- Raspberry Pien kjører en Python-fil som rullerer mellom ulike tabs i nettleseren.
- Ligger et standardsett med tabs i nettsidelenker.py
    - På sikt kan det jo også være spesifikke tabs med feks en gitignored id-fil på pien
- Repoet pulles til Raspberry Pien ved oppstart, og et shellscript kjører Python-fila.
- Endringer i nettsider kan gjøres på repoet og så bare kjøre omstart av Raspberry Pien for å oppdatere.


## Hvordan kjøre?

For å kjøre .py fila på Raspberry Pien ved boot, kjør:

````
sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
````

og legg til følgende linje:

````
@lxterminal -t lxterm -e /home/pi/Desktop/infoskjerm/refresher.sh
````

Husk å gi filen executable rettigheter:

````
chmod +x refresher.sh
````


## Hvordan sette opp Raspberry Pien?

Se fila Oppsett-rpi.md
