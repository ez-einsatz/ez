from django.urls import path

from . import views

urlpatterns = [
    path('', views.Einsatztagebuch.as_view(), name='einsatztagebuch'),
]
