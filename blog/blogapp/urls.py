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
]


'''
path(urlpatter,views.function_name,name)
'''