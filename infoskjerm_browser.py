# python file to keep infoskjerm running and swapping between tabs
import webbrowser
import time
import pyautogui

nettsider = {
    "quarto_infoskjerm": "https://data.ansatt.nav.no/story/6c66a54b-3599-4090-80a1-1a4073900929/index.html#hjem",
    # "grafana_spenn": "https://grafana.nav.cloud.nais.io/d/d1961678-a775-469a-8718-92082ee6f3ba/airflow-profilering?orgId=1&var-namespace=team-spenn-vans&from=now-2d&to=now",
    # "quarto_stonads": "https://data.ansatt.nav.no/story/6c66a54b-3599-4090-80a1-1a4073900929/index.html#stønadsmottakere",
    # "quarto_nye_rader": "https://data.ansatt.nav.no/story/6c66a54b-3599-4090-80a1-1a4073900929/index.html#kpi-nye-rader",
    # "indikator1": "https://data.ansatt.nav.no/story/90383a5a-8cc9-42e2-a916-ec7dc90b3247/pages/detaljert/nav_historikk.html",
    # "ateam_quarto": "https://data.ansatt.nav.no/story/b54e4a30-7fca-491a-ab04-ac93795c7b37/pages/ovr_kompetanse.html",
    # "torden": "https://map.blitzortung.org/#7.01/59.024/11.082/0/1",
    # "damene": "https://data.ansatt.nav.no/story/7ea943c9-ae07-4d75-9b65-d775c05230dc/make_dashboard.html#kvinneandel-i-tech",
    "yr_oslo": "https://www.yr.no/nb/v%C3%A6rvarsel/timetabell/1-72837/Noreg/Oslo/Oslo/Oslo?i=0",
    "nrk": "https://www.nrk.no/nyheter/",
    "quotes": "https://www.goodreads.com/quotes",
    "quotes": "https://zenquotes.io/",
    "delta": "https://delta.nav.no/",
    "picsum1": "https://picsum.photos/1600/800",
    "picsum2": "https://picsum.photos/1600/800",
    "picsum3": "https://picsum.photos/1600/800",

}

mac = False
cmd = "command" if mac else "ctrl"
pause_tid = 60  # seconds


def main():
    # first open google.com to reset the browser, then close it
    webbrowser.open("https://www.google.com")
    time.sleep(2)
    with pyautogui.hold(cmd):
        pyautogui.press("w")
    time.sleep(2)

    # open the quarto to load the connection / login
    webbrowser.open(nettsider["quarto_infoskjerm"])
    time.sleep(30)

    # open all tabs
    for tab in nettsider.values():
        webbrowser.open(tab)
        time.sleep(0.5)

    # on startup the default quarto page is opened, which we don't want
    with pyautogui.hold(cmd):
        pyautogui.press("1")
        time.sleep(1)
        pyautogui.press("w")

    loop = 0
    tab_numbers = [str(i) for i in range(1, len(nettsider) + 1)]

    try:
        while True:
            for number in tab_numbers:
                with pyautogui.hold(cmd):
                    pyautogui.press(number)  # switch tab
                    if loop % 100 == 0:
                        pyautogui.press("r")  # refresh
                time.sleep(pause_tid)
            loop += 1
    except KeyboardInterrupt:
        print("Exiting the loop")
        pass
    except Exception as e:
        print("An error occurred:", e)
        pass

    print("finito")


if __name__ == "__main__":
    main()
