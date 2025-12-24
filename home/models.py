from django.db import models

# Create your models here.
class orderstatus(models.model):
    name=models.charfeild(max_length=50,unique=True)
    class coupon(models.model):
        code=models.charfeild(max_length=50, unique=True)
        discount_percentage=models.decimalfeild(max_digits=5, decimal_places=2)
        is_active = models.booleanfeild(default=True)
        valid_from=models.datefield()
        valid_until=models.datefield()
        def __str__(self):
            return self.code