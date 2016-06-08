Hallo {{ teilnehmer.name }},

unser Klassentreffen findet diesen Samstag statt.
{% if teilnehmer.state == teilnehmer.STATE_PROPABLY %}
Du hast uns noch nicht sicher mitgeteilt, ob du kommst. Teile uns bitte bis
spätestens Donnerstag Vormittag mit, ob du dabei bist.{% endif %}
{% if not teilnehmer.location_current %}
Du hast das Formular für das Klassenbuch noch nicht ausgefüllt, bitte nehme dir
jetzt eine Minute Zeit hierfür, damit ein möglichst vollständiges Klassenbuch
entsteht. {% endif %}Hier nocheinmal der Link, mit dem du die Daten für das
Klassenbuch eintragen kannst: {{ teilnehmer.get_edit_link }}

Hier findest du den aktuellen Entwurf des Klassenbuches:

http://klasse-93.de/show/

{% if teilnehmer.kommt %}
Am Samstag werden wir uns zunächst zu Kaffee und Kuchen in der Cafeteria der
Schule treffen. Bitte gib uns bis Freitag per E-Mail Bescheid, ob und wenn ja
was für einen Kuchen du mitbringst.{% endif %}

Wenn du noch Bilder aus der Schulzeit hast, würden wir uns freuen, wenn du sie
uns zur Verfügung stellen kannst. Der Link zum Hochladen ist:

https://cloud.klasse-93.de/index.php/s/Ff7hI8KSGUhJt1v


Viele Grüße

Lars, Martin und Oskar
