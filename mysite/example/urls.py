from django.contrib import admin
from django.urls import path
from .views import MyView

urlpatterns = [
    path('', MyView.as_view())
]
