from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('', views.wonder,name="wonder"),
    path('demo/',views.second,name='second'),
    path('insert',views.insertdata,name="insert"),
    path('update/<id>',views.updatedata,name="update"),
    path('delete/<id>',views.deletedata,name="delete"),
]
