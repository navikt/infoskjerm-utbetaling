How to infoskjerm (dvh edition)Infoskjerm, altså å bruke de tomme TV-skjermene i bygget til noe visuelt, kan være både artig og nyttig. Det er feks nice å vise et Quarto Dashboard, som kan vise tekst, tall og grafer. Her er en oppskrift laget i mars 2023 med stegene for å få på plass en infoskjerm (av @brynjar.morka.mehlum).

Spørsmål kan stilles i #infoskjerm 

Kortversjon:

* skaff en raspberry pi og sett den opp. Koble til wifi NAV-mob
* Skru av skjermsparer. Sett start-fane til ønsket nettside og velg at Chromium skal åpnes ved start up
* Skaff en servicebruker via Team Arbeidsflate for å få vise Markedsplassen/Grafana :quarto: :grafana: 
* Gå til nettsiden og logg inn. To-faktorautentisering må gjentas hver 30. dag :azure_new: 
* Nå kan du bare skru på mikrokontrolleren på morgenen, så går den inn på Quarto-nettsiden og viser oppdatert informasjon :nice: 


Detaljeversjon:

1. Anskaff en raspberry pi, feks starter kittet her som har alt du trenger under. Finnes sikkert billigere versjoner, men den har alt du trenger. For meg (team Spenn) fikset @petter.dybing betaling.
    1. Du må ha: raspberry pi, hdmi til mikro-hdmi, minnekort, strømkabel
    2. Kjekt å ha: deksel/boks til mikrokontrolleren, vifte, kjølere
2. Følg setup-guide for å sette sammen og starte raspberry pi. Laster ned OS, setter opp bruker. Her må du ha et tastatur, og det er kjekt med en mus (begge med usb-tilkobling).
3. Koble til nettverket NAV-mob, hvor du kan få passord fra en personalleder eller servicetorget. Det er laget et skjult nettverk som heter infoskjerm (ikke det samme som NAV-infoskjerm). 
    1. Jeg fikk ikke til å koble meg på det skjulte nettverket infoskjerm, men det er visst ikke nødvendig, i alle fall ikke for quarto via Markedsplassen. Hvis du vil på det skjulte nettverket infoskjerm kan du høre i #tech-nettverk. 
4. For at mikrokontrolleren ikke skal gå i dvale må du skru av skjermsparer
    1. Last ned xscreensaver med sudo apt-get install xscreensaver,
    2. Kjør sudo raspi-config og skru av "screen blanking" under "display settings"
5. Åpne nettleseren og gå til nettsiden du vil vise.
    1. Du kan automatisk åpne nettleseren på start-up, og så sette ønsket nettside som default i chromium (da er det bare å skru på bryteren så vises skjermen av seg selv). Følg stegene her. 
    2. Dersom du vil vise noe fra Markedsplassen, feks et Quarto Dashboard (eks team Paw, eks team Spenn), så må du ha en type servicebruker for å logge inn, som er en vanlig AD-login. Dette er stegene for å lage en servicebruker:
        1. Opprett en sak i porten (samme hva slags type sak) hvor du skriver at du vil ha en servicebruker til en infoskjerm.
        2. Send melding til Team Arbeidsflate, feks @jon.sverre.karlsen, hvor du skriver at du har opprettet en oppgave. Du får brukernavn (en epostadresse) i Jira-saken og passord på mail.
        3. OBS! Det er ikke mulig å søke etter en data story på Markedsplassen med denne servicebrukeren, så du må skrive inn hele URLen.
        4. Vis data storyen, som kan inneholde grafer fra spørringer mot Oracle.
        5. Logg inn på servicebrukeren med tofaktorautentisering (App/SMS)
    3. Andre sider som Grafana kan vel også vises
    4. Det skal være mulig å bruke utvidelser som revolver-tabs for å bytte mellom et sett av faner, men jeg har ikke fått det til.



Ting jeg knotet mye med:

* Fikk ikke lov å laste ned revolver tabs fordi Chromium var utdatert
* Datamarkedsplassen sitt søk funker ikke, da står det at du ikke har tilgang. Må skrive hele url-en for å komme til en data story
* Skjønte ikke hvilken type servicebruker jeg skulle ha. I noen guider står det at du kan lage servicebruker på repoet gruppetilgang-servicebruker, men det var visst ikke riktig.
* Jeg fikk ikke opp menyvalget for skjermsparer, men sudo raspi-config funket fjell for å skru av dvale.

