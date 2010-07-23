import datetime
from django.db import models

class BasePage(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True,
                                    default=datetime.datetime.today())
  updated_at = models.DateTimeField(auto_now=True,
                                    default=datetime.datetime.today())

  class Meta:
    abstract = True
