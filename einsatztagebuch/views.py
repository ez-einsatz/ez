from django.shortcuts import render
from django.views import generic

from django.contrib.auth.mixins import PermissionRequiredMixin

from . import models

class Einsatztagebuch(PermissionRequiredMixin, generic.ListView):

    model = models.Einsatztagebucheintrag
    template_name = 'einsatztagebuch.html'

    permission_required = 'einsatztagebuch.view_einsatztagebucheintrag'
