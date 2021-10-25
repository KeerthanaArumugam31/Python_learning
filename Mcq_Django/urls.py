from .views import *
from django.urls import path

urlpatterns = [
    path('',login,name='login'),
    path('register',register,name='register'),
    path('registration',registration,name="registration"),
    path('question',question,name='question'),
    path('calculatemark',calculatemark,name='calculatemark'),
    path('checkuser',checkuser,name="checkuser"),
    path('logout',logout,name='logout')
   ]
