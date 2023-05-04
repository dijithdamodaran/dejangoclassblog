from django.db import models

# Create your models here.
class product(models.Model):
    CAT=(('1','Mobile'),('2','Cloths'))
    STAT=(('1','Active'),('0','Inactive'))
    name=models.CharField(max_length=50,verbose_name="Product Name")
    cat=models.CharField(max_length=50,verbose_name="Category",choices=CAT)
    price=models.FloatField(verbose_name="Product Price")
    status=models.CharField(max_length=50,choices=STAT)

    def __str__(self):

        return self.name 