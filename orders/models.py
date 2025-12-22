from django.db import models
class orderstatus(models.model):
    name=models.charfield(max_length=50)
    def __str__(self):
        return self.name
        class order(models.model):
            order_number = models.charfield(max_length=100)
            customer_name = models.charFeild(max_length=100)
            created_at = models.datetimefeild(auto_now_add=True)
            status = models.foreignkey(
                orderstatus,
                on_delete=models.set_null,
                null=True
            )
            def __str__(self):
                return self.order_number
# Create your models here.
