from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,redirect
from django.contrib import messages
from registeration.models import Challan, Police
from datetime import date, datetime
import time
import random
from django.urls import reverse

def initial(email):
    global user
    user = email
    return user

def dt(dat):
    global dated
    dated = dat
    return

def tt(tim):
    global timed
    timed = tim
    return

# Create your views here.
def policelogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        police = Police.objects.filter(email=email,password=password)
        request.session['user_email'] = email
        request.session['referal_url'] = request.META.get("HTTP_REFERER",'/')
        print(police)
        initial(email)
        return policeindex(request)
    else:
        print("not logged in....")
    return render(request, 'policelogin.html')

def default_redirect_view(request):
  return redirect('default_redirect_url')

def login_success_view(request):
  referrer_url = request.session.pop('referrer_url','/')
  return policeindex(request) 

def policeindex(request):
    pemail = request.session.get('user_email')
    police = Police.objects.filter(email=pemail)
    challan = Challan.objects.filter(pemail=pemail)
    elements = {
        'challan' : challan 
    }
    return render(request, 'policeindex.html',elements)

def addchallan(request):
    if request.method == 'POST':
        pemail = request.session.get('user_email')
        demail = request.POST.get('demail')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        reason = request.POST.get('offence')
        fine = request.POST.get('fine')
        d = date.today()
        dt(d)
        t = datetime.now()
        tt(t)
        lt = str(timed.hour) +":"+ str(timed.minute)
        print(pemail)
        #print(police_email)
        print("Hello")
        random_number = random.randint(1, 100)
        print(random_number)
        challan = Challan(issueid=random_number, pemail=pemail,demail=demail,fname=fname,lname=lname, reason=reason,status='Pending',fine=fine,date=dated,time=lt)
        challan.save()
        return redirect(request.META.get('HTTP_REFERER',reverse('default_redirect_view')))
    else:
        print("Not Done....")
    return render(request, 'addChallan.html')