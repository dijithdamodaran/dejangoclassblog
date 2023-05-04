from django.contrib import admin
from blogapp.models import product

# Register your models here.

#admin.site.register(product)

#step1:define modeladmin class inherited from modeladmin class

class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price','cat','status']
    list_filter=['cat','status']

    #step2:register modeladminclass i.e prodectadmin with model prodect in admin

admin.site.register(product,ProductAdmin)
admin.site.site_header="Ecommerce Dashbord"
admin.site.site_title="Ecomm"
admin.site.index_title="Ecommere Administration"
 
