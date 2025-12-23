from django.db import models

# Create your models here.
class orderstatus(models.model):
    name=models.charfeild(max_length=50,unique=True)