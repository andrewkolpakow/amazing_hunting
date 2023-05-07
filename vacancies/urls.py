from django.contrib import admin
from django.urls import path
from vacancies.views import VacancyDetailView, VacancyListView, VacancyCreateView, VacancyUpdateView, VacancyDeleteView

urlpatterns = [
    path("", VacancyListView.as_view()),
    path("<int:pk>/", VacancyDetailView.as_view()),
    path("create/", VacancyCreateView.as_view()),
    path("<int:pk>/update/", VacancyUpdateView.as_view()),
    path("<int:pk>/delete/", VacancyDeleteView.as_view()),
]