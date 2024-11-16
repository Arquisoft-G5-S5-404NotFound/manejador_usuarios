from django.db import models
import uuid

# Create your models here.
class School(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4)
    name = models.CharField(max_length=100)
