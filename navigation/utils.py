from django.utils.safestring import mark_safe

def get_flat_tuples(menu_item, excepted_item=None):
    """
    Returns choices for a menu item and all of its descendants.
    Taken from treemenu.utils
    """
    if menu_item == excepted_item:
        return []
    else:
        choices = [(menu_item.pk, mark_safe(menu_item.caption_with_spacer()))]
        if menu_item.has_children():
            for child in menu_item.children():
                choices += get_flat_tuples(child, excepted_item)
        return choices
