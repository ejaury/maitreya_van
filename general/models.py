import datetime
from django.contrib.contenttypes.models import ContentType
from django.db import models, transaction
from exceptions import NotImplementedError
from maitreya_van.navigation.models import MenuItemExtension
from tagging.fields import TagField
from treemenus.models import MenuItem


class BasePage(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,
        help_text='A "slug" is a unique URL-friendly title \
                  (link name) for an object. (e.g. category Community \
                  Performance can have a slug named "comm-performance",\
                  in which the pages can be accessed via \
                  http://www.mywebsite.com/pages/comm-performance')
    content = models.TextField()
    # TODO: Exclude parent_menu_item field from DB and use a custom Form for it
    parent_menu_item = models.ForeignKey(MenuItem, related_name='+',
        help_text = 'Menu item that this page belongs to (e.g. Dance Class page belongs to "Classes" section)')
    menu_item = models.OneToOneField(MenuItem, null=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True,
        default=datetime.datetime.today())
    updated_at = models.DateTimeField(auto_now=True,
        default=datetime.datetime.today())

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.title

    @transaction.commit_on_success
    def save(self, *args, **kwargs):
        try:
            super(BasePage, self).save(*args, **kwargs)
            menu_kwargs = {
                'parent': self.parent_menu_item,
                'caption': self.title,
                'url': self.get_absolute_url(),
            }
            if self.menu_item is None:
                menu_item = MenuItem(**menu_kwargs)
                menu_item.save()
                self.menu_item = menu_item
                super(BasePage, self).save(*args, **kwargs)
            else:
                for attr, val in menu_kwargs.items():
                    setattr(self.menu_item, attr, val)
                self.menu_item.save()
            menu_item_ext, created = MenuItemExtension.objects.get_or_create(
                menu_item=self.menu_item)
            menu_item_ext.selected_patterns = '^%s$' % self.get_absolute_url()
            menu_item_ext.save()
        except Exception:
            transaction.rollback()
            raise

    def delete(self, *args, **kwargs):
        if self.menu_item:
            try:
                menu_ext = MenuItemExtension.objects.get(menu_item=self.menu_item)
                menu_ext.delete()
            except MenuItemExtension.DoesNotExist:
                pass
            self.menu_item.delete()
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
