# LeistungsdiagnostikApp

## Vorbereitungen für das Programm

1. Ordner erstellen
2. die gegeben Datein: ```load_data.py``` und ```activit.csv``` herunterladen und in den Ordner einfügen
3. einen Sortier-Algorithmus erstellen
4. .gitignore Datei erstellen um ünnotige Datein nicht hochzuladen
4. virtuelle Umgebung erstellen und benötigte Bibliotheken herunterladen
5. Hauptprogramm schreiben um Daten grafisch darzustellen

## Virtuelle Umgebung erstellen
Bezogen auf die Erstellung auf dem MacBook:
Die virtuelle Umgebung kann mithilfe der Kommandozeile erstellt werden, hierzu muss man den folgenden Befehl eingeben:

```python3 -m venv venv```

Anschließend muss diese Virtuelle Umgebung noch aktiviert werden, dies erfolgt durch den Befehl:

```source /venv/bin/activate```

Nun können innerhalb der virtuellen Umgebung alle Bibliotheken die gebraucht werden installiert werden ohne diese direkt auf dem PC zu haben.

## Funktionsweise des Programmes
in dem Programm sort werden die verschiedenen Sortier-Algorithmen erstellt die später in den anderen Programmen gebraucht werden.

load_data importiert die benötigten Bibliotheken und den zuvor erstellten Sortieralgorithmus, 
um die activity.csv-Datei zu öffnen und zu verarbeiten.
Innerhalb des Prgramms wird die Datei geöffnet und in das richtige Format gebracht, anschließend werden die Werte einer Variable zugewiesen daraufhin mit dem Bubblsort Algorithmus sortiert und in umgekehrter Reihenfolge ausgegeben

In dem main-Programm wird die sortierte Liste importiert und mithilfe von matplotlib grafisch ausgegeben.
Die Achsen werden noch wie gewünscht beschriftet um Klarheit über das Diagramm zu schaffen.






