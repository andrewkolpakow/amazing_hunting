from django.contrib import admin
from django.urls import path
from rest_framework import routers
from vacancies.views import VacancyDetailView, VacancyListView, VacancyCreateView, VacancyUpdateView, \
    VacancyDeleteView, UserVacancyDetailView, SkillsViewSet, VacancyLikeView

urlpatterns = [
    path("", VacancyListView.as_view()),
    path("<int:pk>/", VacancyDetailView.as_view()),
    path("create/", VacancyCreateView.as_view()),
    path("<int:pk>/update/", VacancyUpdateView.as_view()),
    path("<int:pk>/delete/", VacancyDeleteView.as_view()),
    path("by_user/", UserVacancyDetailView.as_view()),
    path("like/", VacancyLikeView.as_view()),
]

