from django import template

from core.menu import MENU_ITEMS

register = template.Library()


@register.inclusion_tag("core/menu.html", takes_context=True)
def main_menu(context):
    request = context.get("request")
    items = []
    for item in MENU_ITEMS:
        url = item.url()
        items.append(
            {
                "label": item.label,
                "url": url,
                "active": bool(request and request.path == url),
            }
        )
    return {"menu_items": items}
