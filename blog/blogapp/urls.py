from django.urls import path
from blogapp import views

urlpatterns = [

    path('about',views.about),
    path('contact',views.contact),
    path('edit/<rid>',views.edit),
    path('delete/<rid>',views.delete),
    path('add/<a>/<b>',views.addition),
    path('hello',views.renderhtml),
    path('datatohtml',views.passdatatohello),
    path('home',views.homepage),
    path('aboutnew',views.aboutpage),
    path('addproduct',views.addproduct),
    path('dash',views.dashbord),
    path('catfilter/<cv>',views.catfilter),
    path('statfilter/<sv>',views.statfilter),
    path('sort/<x>',views.sortfilter),
    path('filprice/<x>',views.pricefilter), 
    path('static',views.staticfile),
    path('djforms',views.django_form),
    path('setcookie',views.setcookie),
    path('getcookie',views.getcookie),
    path('multifilter',views.multifilter),
    path('setsession',views.setsession),
    path('getsession',views.getsession),
    path('modelform',views.modelform),
    path('register',views.user_register),
    path('login',views.user_login),
]


'''
path(urlpatter,views.function_name,name)
'''