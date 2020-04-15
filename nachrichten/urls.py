from django.urls import path
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='/nachrichten/nachweisung')),
    path('neu/ein', views.NeueEingehendeNachricht.as_view(), name='neu-ein'),
    path('neu/aus', views.NeueAusgehendeNachricht.as_view(), name='neu-aus'),
    path('neu/notiz', views.NeueNotiz.as_view(), name='neu-notiz'),
    path('<int:pk>/', views.Nachricht.as_view(), name='show'),
    path('nachweisung', views.Nachweisung.as_view(), name='nachweisung'),
]
