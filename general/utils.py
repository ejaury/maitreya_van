from django.conf import settings

from treemenus.models import Menu, MenuItem
from treemenus.utils import get_parent_choices

from maitreya_van.navigation.utils import get_flat_tuples


def get_menu_item_choices(page):
    if hasattr(page, 'get_index_url'):
        url = page.get_index_url()
        root = MenuItem.objects.get(parent=None)
        menu_items = MenuItem.objects.filter(url=url).order_by('level')
        # Return choices for the outermost menu item (menu item with the
        # lowest level - closest to root)
        if menu_items.count() > 0:
            return get_flat_tuples(menu_items[0], page.menu_item)

    # Return all menu items
    menu = Menu.objects.get(name=getattr(settings, 'MAIN_MENU_NAME', 'Main'))
    return get_parent_choices(menu)
