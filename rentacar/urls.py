from django.contrib import admin
from django.urls import path
from .views import CarListCreateView,CarListView

urlpatterns = [
    path('cars/',CarListCreateView.as_view()),
    path('cars-search/<int:pk>',CarListView.as_view()),
]
