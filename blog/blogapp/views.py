from django.shortcuts import render,redirect
from django.http import HttpResponse

def about(request):
    #return HttpResponse("hello this is function based view")
    return redirect('/contact')

def contact(request):
    return HttpResponse("hello this is function based view contact")

def edit(request,rid):
    return HttpResponse("ID to be edited:"+rid)

def delete(request,rid):
    return HttpResponse("ID to be deleted:"+rid)

def addition(request,a,b):
    z=int(a)+int(b)
    return HttpResponse("add two number:"+str(z))

def renderhtml(request):
    return render(request,'hello.html')
#passing data to hello.html file

def passdatatohello(request):
   # content={'data':'hello world'}
    content={}
    content['data']="hello world DTL"
    content['x']=100
    content['y']=20
    content['z']=[1,2,3,4,5]
    
    return render (request,'hello.html',content)

def homepage(request):
    return render(request,'home.html')
def aboutpage(request):
    return render(request,'aboutnew.html')

def addproduct(request):
    return render(request,'addproduct.html')
# Create your views here.
