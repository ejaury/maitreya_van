from django.contrib.contenttypes.models import ContentType
from django.db import models

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
