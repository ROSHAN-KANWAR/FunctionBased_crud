from django.contrib import admin
from django.urls import path,include
from enroll import views

urlpatterns = [
   path("", views.MForm, name="mform"),
   path('delete/<int:id>/', views.delete_data, name="delete"),
   path('<int:id>/', views.edit_data, name="edit"),
  
]