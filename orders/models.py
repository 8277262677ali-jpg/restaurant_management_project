from django.db import models
class menucategory(models.model):
    name=models.charfield(max_length=100,unique=True)
    def__str__(self):
        return self.name