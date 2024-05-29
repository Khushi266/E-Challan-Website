from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('driverlogin/', views.driverlogin, name='driverlogin'),
    path('driverindex/', views.driverindex, name='driverindex'),
    path('delete/<int:id>',views.delete, name='delete'),
    path('default_redirect',views.default_redirect_view, name='default_redirect_view'),
    path('driverlogin/s',views.login_success_view, name = 'login_success_view'),
    path('payment/<int:id>',views.payment, name = 'payment'),
    path('receipt/<int:id>', views.receipt, name = 'receipt'),
    path('receipt_pdf/<int:id>/', views.receipt_pdf, name='receipt_pdf'),
]
