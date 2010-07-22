from django.db import models

class BasePage(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()

  class Meta:
    abstract = True
