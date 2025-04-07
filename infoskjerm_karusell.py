import time
import socket
import pyautogui
import webbrowser

import nettsidelenker
nettsider = nettsidelenker.nettsider

mac = False
cmd = "command" if mac else "ctrl"
tid_i_hver_fane = 60  # seconds


# åpner google.com for å slippe "vil du gjenåpne faner" melding
webbrowser.open("https://www.google.com")
time.sleep(4)
with pyautogui.hold(cmd):
    pyautogui.press("w")
time.sleep(1)


# åpner en nav-side som lukkes etter 30 sekunder, som løser redirect ved AD-innlogging
temp_nav_side = "https://data.ansatt.nav.no/quarto/0b700511-f50c-4059-b519-32fb19637bae/bemanning.html"
webbrowser.open(temp_nav_side)
time.sleep(10)

# åpne alle faner og lukker temp_nav_side
for tab in nettsider:
    webbrowser.open(tab)
    time.sleep(1)
with pyautogui.hold(cmd):
    pyautogui.press("1")
    time.sleep(0.5)
    pyautogui.press("w")

# gå i fullskjerm
pyautogui.hotkey("f11")

loop = 0
alle_fanenummerene = [str(i + 1) for i in range(len(nettsider))]

try:
    while True:
        for fanenummer in alle_fanenummerene:
            with pyautogui.hold(cmd):
                pyautogui.press(fanenummer)  # bytter fane med cmd+1, cmd+2 osv
                if loop % 10 == 0:
                    pyautogui.press("r")  # kjører en refresh av fanen innimellom
            time.sleep(tid_i_hver_fane)
        loop += 1
except KeyboardInterrupt:  # tillater å stoppe loopen med ctrl+c
    print("Avslutter loopen mellom faner")
    pass
except Exception as e:
    print("En feil oppstod:", e)
    pass

print("Avsluttet infoskjerm_karusell.py klokka", time.strftime("%H:%M:%S"))
