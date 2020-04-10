from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('neu', views.NachrichtCreate.as_view(), name='create'),
    path('nachweisung', views.Nachweisung.as_view(), name='nachweisung'),
]
