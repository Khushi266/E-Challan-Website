from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('policelogin/', views.policelogin, name = 'policelogin'),
    path('policeindex/', views.policeindex, name='policeindex'),
    path('addchallan/',views.addchallan, name= 'addchallan'),
    path('default_redirect',views.default_redirect_view, name='default_redirect_view'),
    path('policelogin/success',views.login_success_view, name = 'login_success_view'),
]
