from django.db import models

# Create your models here.
class product(models.Model):
    name=models.CharField(max_length=50)
    cat=models.CharField(max_length=50)
    price=models.FloatField()
    status=models.CharField(max_length=50)