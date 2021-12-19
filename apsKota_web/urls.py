from django.contrib import admin
from django.urls import path
from .views import *
from apsKota_web import views

urlpatterns = [
    path("", views.home, name="home"),    
    path("post", views.post, name="post"), 
    path("<slug:slug>/", post_detail, name="post_detail")

]