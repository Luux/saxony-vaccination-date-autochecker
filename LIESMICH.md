# Impftermin-Autochecker für Sachsen

Dieses Tool prüft regelmäßig freie Impftermine von Impfzentren in Sachsen, indem es auf die unter https://www.countee.ch/app/de/counter/impfee/_iz_sachsen verfügbaren Live-Counter zugreift.
Sobald mehr Impftermine verfügbar sind als bei der letzten Überprüfung, erhaltet ihr eine Benachrichtigung.

Dieses Tool registriert euch NICHT für einen Impftermin. Allerdings könnt ihr es im Hintergrund laufen lassen, sodass ihr nicht permanent selbst die countee-Seite überwachen müsst.

![image](https://user-images.githubusercontent.com/15156652/117510088-b9f3a700-af8b-11eb-84c4-11c531d17c4c.png)




Installation (Standalone)
------------------------

1. Ladet die neueste Version unter https://github.com/Luux/saxony-vaccination-date-autochecker/releases herunter (saxony-vaccination-date-autochecker.zip).
2. Startet das Programm durch einen Doppelklick auf eine der .bat-Starter-Dateien (z.B. dresden.bat für das Dresdner Impfzentrum).


Mein Antivirus/SmartScreen meldet sich, was soll ich tun?
-------------------------------------------------------------

Keine Sorge, das sind Fehlalarme. Technischer Hintergrund: Die .exe wird mit pyinstaller gebaut, welches nur das Skript aus diesem Repository zusammen mit allen Abhängigkeiten einschließlich der Python-Laufzeit in eine einzige ausführbare Datei bündelt. Executables, die mit pyinstaller erstellt wurden, werden oftmals von Windows SmartScreen oder Antivirenprogrammen verdächtigt (siehe z.B. https://github.com/pyinstaller/pyinstaller/issues/4852).

Sollte SmartScreen den Start blockieren:

![image](https://user-images.githubusercontent.com/15156652/117507377-389a1580-af87-11eb-885d-5a48d432eb9b.png)

Rechtsklick auf die jeweilige .bat (etwa dresden.bat) -> Eigenschaften -> Zulassen -> OK

![image](https://user-images.githubusercontent.com/15156652/117539381-a63b5580-b00a-11eb-8ecd-78639c9bac01.png)



Alternativ kann das python-Skript auch direkt gestartet werden (s. u.).


Installation (Source, für erfahrenere Nutzer)
---------------------

1. Python installieren: https://www.python.org/

2. Sicherstellen, dass python in der PATH-Umgebungsvariable liegt

3. ```pip install -r requirements.txt```

4. Starten des Skripts. Beispiel für die Verwendung:
```python saxony_vaccination_date_autochecker/autocheck_countee-py "Dresden IZ"```


Optionen:

```
python .saxony_vaccination_date_autochecker\autocheck_countee.py --help
Benutzung: autocheck_countee.py [-h] [--intervall INTERVALL] vaccination_center

positionale Argumente:
  vaccination_center Der Name des Impfzentrums, wie er in countee angezeigt wird.
                        Beispiel: "Dresden IZ".

optionale Argumente:
  -h, --help Hilfe anzeigen
  --intervall INTERVALL
                        Prüfintervall in Minuten (Voreinstellung: 10).
```
