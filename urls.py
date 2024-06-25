from django.urls import path
from ChefGenAI.views import Home #from ChefGenAI import views

urlpatterns=[
    path('',Home.as_view(), name='home')
]

