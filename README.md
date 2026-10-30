# oshdas

open-source health data assistant

Django-Projekt mit Login, Menü und Erfassung von Vitalwerten und Gemütszustand.

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env        # Werte anpassen (siehe unten)
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Konfiguration (.env)

Alle sensiblen Werte werden aus Umgebungsvariablen gelesen (Vorlage:
`.env.example`). Ohne `DATABASE_URL` greift ein SQLite-Fallback für die
lokale Entwicklung.

| Variable | Bedeutung |
|---|---|
| `DJANGO_SECRET_KEY` | Geheimer Schlüssel (erzeugen mit `get_random_secret_key()`) |
| `DJANGO_DEBUG` | `1` = Development, `0` = Production |
| `DJANGO_ALLOWED_HOSTS` | Komma-getrennte erlaubte Hosts |
| `DATABASE_URL` | `postgres://user:passwort@host:port/dbname` |

## TimescaleDB

Die Migrationen `vitals/migrations/0002_hypertable.py` und
`mood/migrations/0002_hypertable.py` konvertieren die Tabellen
`vitals_vitalmeasurement` (Partitionierung: `measured_at`) und
`mood_moodrecord` (Partitionierung: `recorded_at`) automatisch in
Hypertables – nur wenn eine PostgreSQL-Verbindung mit installierter
TimescaleDB-Erweiterung erkannt wird. Vorher muss in der Datenbank einmalig
`CREATE EXTENSION IF NOT EXISTS timescaledb;` ausgeführt werden (als Superuser).

Jeder Eintrag speichert den Benutzernamen (`user`) und einen Zeitstempel
(`measured_at` bzw. `recorded_at`).

## Menü erweitern

Neue Menüpunkte in `core/menu.py` in der Liste `MENU_ITEMS` ergänzen:

```python
MenuItem("Neuer Punkt", lambda: reverse("app:view_name"))
```

Danach erscheint der Punkt automatisch in der linken Seitenleiste. Neue
Seiten sollten von `LoginRequiredMixin` erben.

## Fragen zum Gemütszustand erweitern

Fragen werden dynamisch aus der Datenbank gelesen (`mood_moodquestion`).
Ergänzen via Django-Admin (`/admin/`) oder Shell:

```python
from mood.models import MoodQuestion
MoodQuestion.objects.create(text="Wie geht es Ihnen?", order=5)
```

`order` bestimmt die Reihenfolge, `is_active=False` deaktiviert eine Frage.

## Struktur

- `core` – Login/Logout, Übersichtsseite, Menü-Registry
- `vitals` – Blutdruck, Puls, Körpertemperatur
- `mood` – Gemütszustand: Fragen + Antworten (5-stufige Skala)
