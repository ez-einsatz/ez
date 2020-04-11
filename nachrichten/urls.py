from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('neu/ein', views.NeueEingehendeNachricht.as_view(), name='neu-ein'),
    path('neu/aus', views.NeueAusgehendeNachricht.as_view(), name='neu-aus'),
    path('neu/notiz', views.NeueNotiz.as_view(), name='neu-notiz'),
    path('<int:pk>/', views.Nachricht.as_view(), name='show'),
    path('nachweisung', views.Nachweisung.as_view(), name='nachweisung'),
]
