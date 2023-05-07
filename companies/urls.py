from django.contrib import admin
from django.urls import path
from companies import views

urlpatterns = [
    path("<int:pk>/image/", views.CompanyImageView.as_view()),
]