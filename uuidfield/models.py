from django.db import models
from fields import UUIDField

class AutoUUIDPk(models.Model):
    class Meta:
        abstract = True
    
    id = UUIDField(primary_key=True, auto=True)