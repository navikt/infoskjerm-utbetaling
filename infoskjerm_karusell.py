import time
import pyautogui
import webbrowser

import nettsidelenker
nettsider = nettsidelenker.standardsider  # default

# dette er filteret for hvilke sider som skal vises i nettsidelenker.py
try:
    import aktive_sider
    nettsider = []
    for liste in aktive_sider.vis_følgende_lister_med_sider:
        if liste == "standardsider":
            nettsider += nettsidelenker.standardsider
        elif liste == "uføre":
            nettsider += nettsidelenker.uføre
        elif liste == "alderspensjon":
            nettsider += nettsidelenker.alderspensjon
        else:
            print(f"Ukjent liste: {liste}")
except ImportError:
    print("aktive_sider.py ble ikke funnet. Ingen ekstra sider åpnes, kun standardsider.")
    pass

mac = False
cmd = "command" if mac else "ctrl"
tid_i_hver_fane = 20  # seconds


# åpner google.com for å slippe "vil du gjenåpne faner" melding
webbrowser.get("chromium-browser").open("https://www.google.com")
time.sleep(4)
with pyautogui.hold(cmd):
    pyautogui.press("w")
time.sleep(1)

# åpner en innlogget nav-side som lukkes etter litt. Det løser redirect ved AD-innlogging
temp_nav_side = "https://data.ansatt.nav.no/quarto/0b700511-f50c-4059-b519-32fb19637bae/bemanning.html"
webbrowser.get("chromium-browser").open(temp_nav_side)
time.sleep(10)

# åpne alle faner og lukker temp_nav_side
for tab in nettsider:
    webbrowser.get("chromium-browser").open(tab)
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
                if loop % 100 == 0:
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
