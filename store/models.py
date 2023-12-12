from django.db import models
import uuid

# Create your models here.

class Product(models.Model):
    id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    name = models.CharField(max_length=300,null=False,blank=False)
    author = models.CharField(max_length=300,null=False,blank=False)
    
