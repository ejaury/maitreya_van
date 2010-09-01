import datetime
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from exceptions import NotImplementedError
from maitreya_van.navigation.models import MenuItemExtension
from tagging.fields import TagField
from treemenus.models import Menu, MenuItem

class BasePage(models.Model):
  title = models.CharField(max_length=100)
  slug = models.SlugField(unique=True,
                          help_text='A "slug" is a unique URL-friendly title \
                          (link name) for an object. (e.g. category Community \
                          Performance can have a slug named "comm-performance",\
                          in which the pages can be accessed via \
                          http://www.mywebsite.com/pages/comm-performance')
  content = models.TextField()
  parent_menu_item = models.ForeignKey(MenuItem, help_text = 'Menu item that \
    this page belongs to (e.g. Dance Class page belongs to "Classes" section)')
  created_at = models.DateTimeField(auto_now_add=True,
                                    default=datetime.datetime.today())
  updated_at = models.DateTimeField(auto_now=True,
                                    default=datetime.datetime.today())

  class Meta:
    abstract = True

  def __unicode__(self):
    return self.title

  def save(self, *args, **kwargs):
    new = True
    if self.id:
      new = False
    super(BasePage, self).save(*args, **kwargs)

    # add this object to treemenu list if it's new
    if new:
      menu_item = MenuItem(parent=self.parent_menu_item,
                           caption=self.title,
                           url=self.get_absolute_url())
      menu_item.save()
      menu_item_ext = MenuItemExtension(menu_item=menu_item,
                                        selected_patterns='^%s$' % self.get_absolute_url())
      menu_item_ext.save()

  def delete(self, *args, **kwargs):
    try:
      menu_item = MenuItem.objects.get(url=self.get_absolute_url())
      menu_item_ext = MenuItemExtension.objects.get(menu_item=menu_item)
      menu_item_ext.delete()
      menu_item.delete()
    except ObjectDoesNotExist:
      pass
    super(BasePage, self).delete(*args, **kwargs)

  @models.permalink
  def get_absolute_url(self):
    raise NotImplementedError


class TaggablePage(BasePage):
  tags = TagField(help_text='Separate tags with spaces, put quotes around \
                  multiple-word tags.',
                  verbose_name=('tags'))

  class Meta:
    abstract = True


class Category(models.Model):
  content_type = models.ForeignKey(ContentType)
  name = models.CharField(max_length=50, unique=True)
  slug = models.SlugField(unique=True,
                          help_text='A "slug" is a unique URL-friendly title \
                          (link name) for an object. (e.g. category Community \
                          Performance can have a slug named "comm-performance",\
                          in which the pages can be accessed via \
                          http://www.mywebsite.com/category/comm-performance')

  def __unicode__(self):
    return '%s: %s' % (self.content_type.name, self.name)

  class Meta:
    ordering = ['content_type', 'name']
    verbose_name_plural = 'Categories'
