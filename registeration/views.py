from django.shortcuts import render,redirect
from .models import Challan, Police
# Create your views here.
def register(request):
    if request.method == 'POST':
        print("Hello")
        email = request.POST.get('email')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        password = request.POST.get('password')
        print(email)
        print(fname)
        police = Police(email=email,fname=fname,lname=lname,password=password)
        police.save()
        print("Done")
        return redirect('policelogin')
    else:
        print("Not Done")
    return render(request, 'register.html')