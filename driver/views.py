from django.shortcuts import render,redirect
from registeration.models import Challan,Police
from django.urls import reverse
from django.template import loader
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from django.contrib import messages

# Create your views here.
def driverlogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        request.session['user_email'] = email
        
        driver = Challan.objects.filter(demail=email)
        request.session['user_email'] = email
        if driver:
            return driverindex(request)
        else:
            print("not logged in....")
    return render(request, 'driverlogin.html')



def driverindex(request):
    demail = request.session.get('user_email')
    print(demail)
    challan = Challan.objects.filter(demail=demail)
    print(challan)
    elements = {
        'challan' : challan 
    }
    return render(request, 'driverindex.html',elements)

def default_redirect_view(request):
  return redirect('default_redirect_url')

def login_success_view(request):
  referrer_url = request.session.pop('referrer_url','/')
  return driverindex(request) 

def delete(request,id):
  print("Hello")
  print(id)
  challan = Challan.objects.get(issueid = id)
  print(challan)
  challan.delete()
  return redirect(request.META.get('HTTP_REFERER',reverse('default_redirect_view')))

def payment(request,id):
  print("Hello")
  print(id)
  challan = Challan.objects.get(issueid = id)
  print(challan)
  challan.status = 'Paid'
  challan.save()
  messages.success(request,'Payment status upadated successfully.')
  return redirect(request.META.get('HTTP_REFERER', reverse('default_redirect_view')))


def receipt(request,id):
  print("Hello")
  print(id)
  challan = Challan.objects.get(issueid = id)
  print(challan)
  elements = {
        'challan' : challan,
  }
  return render(request,'receipt.html',elements)

def receipt_pdf(request, id):
    # Assuming Challan is your model and you want to generate receipt for a specific challan
  challan = Challan.objects.get(issueid=id)

    # Create a PDF response
  response = HttpResponse(content_type='application/pdf')
  response['Content-Disposition'] = 'filename="receipt.pdf"'

    # Create a PDF document
  p = canvas.Canvas(response)
  p.drawString(100, 800, "Receipt")
  p.drawString(100, 750, f"Challan ID: {challan.issueid}")
  p.drawString(100, 700, f"Issued By: {challan.pemail}")
  p.drawString(100, 650, f"Name: {challan.fname} {challan.lname}")
  p.drawString(100, 600, f"Violation: {challan.reason}")
  p.drawString(100, 550, f"Amount: {challan.fine}")
  p.drawString(100, 500, f"Payment Status: {challan.status}")

    # Save the PDF document
  p.showPage()
  p.save()
  return response