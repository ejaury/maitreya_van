from django.db import models

class PluggableQuerySetManager(models.Manager):
    """Model manager that allows user to plug a custom queryset class"""
    def __init__(self, qs_class=models.query.QuerySet):
        self.qs_class = qs_class
        super(PluggableQuerySetManager, self).__init__()

    def get_query_set(self):
        return self.qs_class(self.model, using=self._db)
