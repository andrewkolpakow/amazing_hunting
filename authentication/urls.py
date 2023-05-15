from django.urls import path
from authentication import views

urlpatterns = [
    path("create/", views.UserCreateView.as_view()),
]