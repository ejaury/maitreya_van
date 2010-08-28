import datetime
from django.contrib.contenttypes.models import ContentType
from django.db import models
from exceptions import NotImplementedError
from tagging.fields import TagField

class BasePage(models.Model):
  title = models.CharField(max_length=100)
  slug = models.SlugField(unique=True,
                          help_text='A "slug" is a unique URL-friendly title \
                          (link name) for an object. (e.g. category Community \
                          Performance can have a slug named "comm-performance",\
                          in which the pages can be accessed via \
                          http://www.mywebsite.com/pages/comm-performance')
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True,
                                    default=datetime.datetime.today())
  updated_at = models.DateTimeField(auto_now=True,
                                    default=datetime.datetime.today())

  class Meta:
    abstract = True

  def __unicode__(self):
    return self.title

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
