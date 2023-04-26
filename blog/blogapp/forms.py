from django import forms


class EmpFormClass(forms.Form):

    empname=forms.CharField(max_length=50)
    mobile=forms.IntegerField()
    department=forms.CharField(max_length=50)
    date_of_joining=forms.DateField(widget=forms.DateInput(attrs={'type' : 'date'}))
