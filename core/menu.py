from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class MenuItem:
    label: str
    url: Callable[[], str]

    def url_str(self):
        return self.url()


def _home():
    from django.urls import reverse

    return reverse("home")


def _vitals():
    from django.urls import reverse

    return reverse("vitals:create")


def _mood():
    from django.urls import reverse

    return reverse("mood:create")


# Neue Menüpunkte einfach hier ergänzen:
# MenuItem("Label", lambda: reverse("app:view_name"))
MENU_ITEMS = [
    MenuItem("Übersicht", _home),
    MenuItem("Vitalwerte", _vitals),
    MenuItem("Gemütszustand", _mood),
]
