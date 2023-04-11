from django.shortcuts import render,redirect
from django.http import HttpResponse
from blogapp.models import product
def about(request):
    #return HttpResponse("hello this is function based view")
    return redirect('/contact')

def contact(request):
    return HttpResponse("hello this is function based view contact")

def edit(request,rid):
    p=product.objects.filter(id=rid)
    return HttpResponse("ID to be edited:"+rid)

def delete(request,rid):
    p=product.objects.filter(id=rid)
    #print(p)
    p.delete()
    return redirect('/dash')

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
    print("method=",request.method)
    if request.method=="POST":
        product_name=request.POST["pname"]
        cat=request.POST["cat"]
        amount=request.POST["amd"]
        stat=request.POST["status"]
        #print("POST request in post setion")
        #print("product name:",product_name)
        #print("catagory name:",cat)
        #print("price:",price)
        #print("status:",status)
        #create model class objet
        p=product.objects.create(name=product_name,cat=cat,price=amount,status=stat)
        #print(p)
        p.save()
        #return HttpResponse("record inserted successfully")
        return redirect('/dash')
    
    else:
        print("get request in else section")
    return render(request,'addproduct.html')

def dashbord(request):
    qset=product.objects.all()
    #print(qset) 
    content={}
    content['data']=qset
    return render(request,'dashboard.html',content)
# Create your views here.
def staticfile(request):
    return render(request,'learnstatic.html')