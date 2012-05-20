from django.db import models

class Color(models.Model):
    name = models.CharField(max_length=20)
    hex = models.CharField(max_length=6)

    class Meta:
        ordering = ('hex',)

    def __unicode__(self):
        return self.name
