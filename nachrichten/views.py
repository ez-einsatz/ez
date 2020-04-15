from django.shortcuts import render
from django.views import generic

from django.http import HttpResponse
from django.template import loader

from django.contrib.auth.mixins import PermissionRequiredMixin

from . import models, forms

class NeueEingehendeNachricht(PermissionRequiredMixin, generic.CreateView):
    model = models.Nachricht
    form_class = forms.NeueEingehendeNachricht
    template_name = 'form.html'

    permission_required = 'nachrichten.add_nachricht'

    def form_valid(self, form):
        form.instance.richtung = 'E'
        return super().form_valid(form)

class NeueAusgehendeNachricht(PermissionRequiredMixin, generic.CreateView):
    model = models.Nachricht
    form_class = forms.NeueAusgehendeNachricht
    template_name = 'form.html'

    permission_required = 'nachrichten.add_nachricht'

    def form_valid(self, form):
        form.instance.richtung = 'A'
        return super().form_valid(form)

class NeueNotiz(PermissionRequiredMixin, generic.CreateView):
    model = models.Nachricht
    form_class = forms.NeueNotiz
    template_name = 'form.html'

    permission_required = 'nachrichten.add_nachricht'

    def form_valid(self, form):
        form.instance.notiz = True
        return super().form_valid(form)

class Nachricht(PermissionRequiredMixin, generic.UpdateView):
    model = models.Nachricht
    form_class = forms.Nachricht
    template_name = 'nachricht.html'

    permission_required = 'nachrichten.change_nachricht'

class Nachweisung(PermissionRequiredMixin, generic.ListView):

    model = models.Nachricht
    template_name = 'nachweisung.html'

    permission_required = 'nachrichten.view_nachricht'

    #paginate_by = 100  # if pagination is desired

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     #context['now'] = timezone.now()
    #     return context
