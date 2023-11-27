from django.db import models

# Create your models here.
class Item(models.Model):
    product_name = models.CharField(max_length=100)
    voltage = models.CharField(max_length=100)
    power = models.IntegerField()
    purpose = models.CharField(max_length=300)
    cost = models.IntegerField()

    def __str__(self):
        return self.product_name