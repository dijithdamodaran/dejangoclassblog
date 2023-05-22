from django import forms
from blogapp.models import product


class EmpFormClass(forms.Form):

    empname=forms.CharField(max_length=50)
    mobile=forms.IntegerField()
    department=forms.CharField(max_length=50)
    date_of_joining=forms.DateField(widget=forms.DateInput(attrs={'type' : 'date'}))


class ProductForm(forms.ModelForm):
    name=forms.CharField(max_length=50)
    cat=forms.CharField(max_length=50)
    price=forms.FloatField()
    status=forms.CharField(max_length=50)

    class Meta:
        model=product
        fields=['name','cat','price','status']
 