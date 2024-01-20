from django.shortcuts import render,redirect
from django.http import HttpResponse
from app1.models import tbl_register,tbl_category,tbl_event,tbl_payment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout
import os

def index(request):
    return render(request,'index.html')

def admin(request):
    return render(request,'admin.html')

def gold(request):
    return render(request,'gold.html')

def plat(request):
    return render(request,'plat.html')

def diamond(request):
    return render(request,'diamond.html')

def about(request):
    return render(request,'about.html')

def payment(request,id,event_name,pr):
    e=event_name
    uid=request.session['user_id']
    total_amount=pr
    if request.method=='POST':
        booking_id=id
        event_name=event_name
        q=tbl_payment(booking_id=booking_id,event_name=e,price=total_amount,status="Paid",user_id=uid)
        q.save()   
        q1=tbl_event.objects.get(id=booking_id) 
        q1.status="Paid"
        q1.save()
        return HttpResponse('<script>alert("Payment Success"),window.location="/myEvent/";</script>')
    return render(request,'payment.html',{'a':total_amount})

def history(request):
    uid=request.session['user_id']
    q=tbl_payment.objects.filter(user_id=uid)
    return render(request,'history.html',{'e':q})

def login(request):
    if request.method=="POST":
        u=request.POST['uname']
        v=request.POST['password']
        au=authenticate(username=u,password=v)
        request.session["user_id"]=u
        if au is not None and au.is_superuser==0:
            return redirect(mainPage)
        elif au is not None and au.is_superuser==1:
            return render(request,"admin.html")
        else:
            return HttpResponse('<script>alert("Incorrect Login"),window.location="/login/";</script>')
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        a=request.POST['uname']
        b=request.POST['email']
        c=request.POST['phone']
        d=request.POST['password']
        q=tbl_register(uname=a,email=b,phone=c)
        data=User(username=a)
        data.set_password(d)
        data.save()
        q.save()
        return HttpResponse('<script>alert("Sucess"),window.location="/login/";</script>')
    return render(request,'register.html')

def viewUser(request):
    s=tbl_register.objects.all()
    return render(request,'viewUser.html',{'key2':s})

def delete(request,id):
    a=tbl_register.objects.get(id=id)
    a.delete()
    return HttpResponse('<script>alert("Sucess"),window.location="/viewUser";</script>')

def update(request,id):
    a=tbl_register.objects.get(id=id)
    if request.method=='POST':
        a.uname=request.POST['uname']
        a.email=request.POST['email']
        a.phone=request.POST['phone']
        a.save()
        return HttpResponse('<script>alert("Sucessfully Updated"),window.location="/viewUser";</script>')
    return render(request,'viewUser.html',{'key1':a})

def mainPage(request):
    q=tbl_category.objects.all()
    return render(request,'mainPage.html',{'c':q})

def logOut(request):
    logout(request)
    return redirect("/login/")

def addCategory(request):
    if request.method=='POST':
        a=request.POST['ctype']
        b=request.FILES['img']
        c=request.POST['food']
        d=request.POST['price']
        q=tbl_category(category_type=a,image=b,food=c,price=d)
        q.save()
        return HttpResponse('<script>alert("Sucess"),window.location="/adminPage/";</script>')
    return render(request,'addcategory.html')
 
def viewCategory(request):
    s=tbl_category.objects.all()
    return render(request,'viewcategory.html',{'x':s})

def deleteCategory(request,id):
    a=tbl_category.objects.get(id=id)
    a.delete()
    return HttpResponse('<script>alert("Sucess"),window.location="/viewCategory";</script>')

def updateCategory(request,id):
    a=tbl_category.objects.get(id=id)
    if request.method=='POST':
        a.category_type=request.POST['type']
        a.food=request.POST['food']
        a.price=request.POST['price']
        if len(request.FILES)!=0:
            if len(a.image)>0:
                os.remove(a.image.path)
                a.image=request.FILES['img']
                a.save()
        return HttpResponse('<script>alert("Sucess"),window.location="/viewCategory";</script>')
    return render(request,'viewCategory.html',{'key1':a})

def choosePlan(request,id):
    q=tbl_category.objects.get(id=id)
    print(type(q.price))
    uid=request.session['user_id']
    if request.method=='POST':
        a=request.POST['event_name']
        b=request.POST['hotel_name']
        c=request.POST['location']
        d=request.POST['date']
        e=request.POST['time']
        f=request.POST['people_count']
        g=request.POST['plan']
        h=request.POST['pr']
        i=request.POST['fp']
        amt=int(i)*int(f)
        total=int(amt)+int(h)
        print(total)
        q=tbl_event(plan_name=g,event_name=a,hotel_name=b,location=c,date=d,time=e,people_count=f,user_id=uid,total_amount=total,status="Pending")
        q.save()
        return HttpResponse('<script>alert("Request Sended"),window.location="/mainPage/";</script>')
    return render(request,'choose.html',{'c':q})

def viewRequest(request):
    s=tbl_event.objects.all()
    return render(request,'viewRequest.html',{'key2':s})

def approve(request,id):
    r_id=id
    q=tbl_event.objects.get(id=r_id)
    q.status="Approved"
    q.save()
    return HttpResponse('<script>alert("Request Accepted"),window.location="/viewRequest/";</script>')

def reject(request,id):
    r_id=id
    q=tbl_event.objects.get(id=r_id)
    q.status="Rejected"
    q.save()
    return HttpResponse('<script>alert("Request Rejected"),window.location="/viewRequest/";</script>')

def myEvent(request):
    uid=request.session['user_id']
    q=tbl_event.objects.filter(user_id=uid)
   
    return render(request,'myEvent.html',{'e':q})

