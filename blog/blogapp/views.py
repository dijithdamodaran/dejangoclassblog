from django.shortcuts import render,redirect
from django.http import HttpResponse
from blogapp.models import product
from blogapp.forms import EmpFormClass


def about(request):
    #return HttpResponse("hello this is function based view")
    return redirect('/contact')

def contact(request):
    return HttpResponse("hello this is function based view contact")

def edit(request,rid):
    if request.method == "POST":
    
        #fetch new changes from the form and 
        product_name=request.POST['pname']
        pcat=request.POST['cat']
        amount=request.POST['amd']
        stat=request.POST['status']
        print(product_name)
        p=product.objects.filter(id=rid)
        p.update(name=product_name,cat=pcat,price=amount,status=stat )
        return redirect('/dash')

        # update it in the database
    else:
        
        #send current details along with form for
        p=product.objects.filter(id=rid)
        content={}
        content['data']=p 
        return render(request,'edit.html',content)
    #p=product.objects.filter(id=rid)
    #return HttpResponse("ID to be edited:"+rid)


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

def setcookie(request):
        res=render(request,'setcookie.html')
        res.set_cookie('name','Itvedant')
        res.set_cookie('rollno','34') 

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

#filters start
def catfilter(request,cv):
    p=product.objects.filter(cat=cv)
    #print(p)
    content={}
    content['data']=p
    return render(request,'dashboard.html',content)

def statfilter(request,sv):
    p=product.objects.filter(status=sv)
    #print(p)
    content={}
    content['data']=p
    return render(request,'dashboard.html',content)


def sortfilter(request,x):
    if x=='0':
        p=product.objects.order_by('price')

    else:
        p=product.objects.order_by('-price')

    content={}
    content['data']=p
    return render(request,'dashboard.html',content) 
    


# Create your views here.
def staticfile(request):
    return render(request,'learnstatic.html')

def django_form(request):

    if request.method=="POST":
        name=request.POST['empname']
        mob=request.POST['mobile']
        dept=request.POST['department']
        dt=request.POST['date_of_joining']
        print("employee:",name)
        print("Mobile:",mob)
        print("department:",dept)
        print("date of joining:",dt)

    else:

        dfobj=EmpFormClass()
        #print(dfobj)
        content={}
        content['form']=dfobj
        return render(request,'empform.html',content)
    
    



