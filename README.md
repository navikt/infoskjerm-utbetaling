Filer til infoskjermen på kontoret


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