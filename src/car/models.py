from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL

class car(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=120)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name