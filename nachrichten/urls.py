from django.urls import path
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='/nachrichten/nachweisung')),
    path('neu/ein', views.NeueEingehendeNachricht.as_view(), name='neu-ein'),
    path('neu/aus', views.NeueAusgehendeNachricht.as_view(), name='neu-aus'),
    path('neu/notiz', views.NeueNotiz.as_view(), name='neu-notiz'),
    path('neu/mail', views.NeueMail.as_view(), name='neu-mail'),
    path('<int:pk>/annahmevermerk', views.Annahmevermerk.as_view(), name='annahmevermerk'),
    path('<int:pk>/befoerderungsvermerk', views.Befoerderungsvermerk.as_view(), name='befoerderungsvermerk'),
    path('<int:pk>/sichtungsvermerk', views.Sichtungsvermerk.as_view(), name='sichtungsvermerk'),
    path('<int:pk>/verteilungsvermerk', views.Verteilungsvermerk.as_view(), name='verteilungsvermerk'),
    path('<int:pk>/', views.Nachricht.as_view(), name='show'),
    path('nachweisung', views.Nachweisung.as_view(), name='nachweisung'),
    path('ausgang', views.Ausgang.as_view(), name='ausgang'),
]
