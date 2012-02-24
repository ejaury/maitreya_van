from django.db import models
from treemenus.models import MenuItem

class MenuItemExtension(models.Model):
  menu_item = models.OneToOneField(MenuItem, related_name="extension")
  selected_patterns = models.TextField(blank=True)

  def __unicode__(self):
      return self.menu_item.caption
