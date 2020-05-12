from django.shortcuts import render
from django.views import generic

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from django.contrib.auth.mixins import PermissionRequiredMixin

from . import models, forms

from django.db import transaction

class NeueEingehendeNachricht(PermissionRequiredMixin, generic.CreateView):
    model = models.Nachricht
    form_class = forms.NeueEingehendeNachricht
    template_name = 'form.html'

    permission_required = 'nachrichten.add_nachricht'

    @transaction.atomic
    def form_valid(self, form):
        form.instance.richtung = 'E'
        form.instance.aufnahmevermerk = models.Aufnahmevermerk(
            benutzer=self.request.user,
            weg=form.cleaned_data['aufnahmeweg'],
        )
        form.instance.save()
        form.instance.aufnahmevermerk.nachricht=form.instance
        form.instance.aufnahmevermerk.save()
        return HttpResponseRedirect(form.instance.get_absolute_url())

class NeueAusgehendeNachricht(PermissionRequiredMixin, generic.CreateView):
    model = models.Nachricht
    form_class = forms.NeueAusgehendeNachricht
    template_name = 'form.html'

    permission_required = 'nachrichten.add_nachricht'

    def form_valid(self, form):
        form.instance.richtung = 'A'
        return super().form_valid(form)

class NeueMail(PermissionRequiredMixin, generic.CreateView):
    model = models.Nachricht
    form_class = forms.NeueMail
    template_name = 'form.html'

    permission_required = 'nachrichten.add_nachricht'

    def form_valid(self, form):
        form.instance.notiz = True
        return super().form_valid(form)

class NeueNotiz(PermissionRequiredMixin, generic.CreateView):
    model = models.Nachricht
    form_class = forms.NeueNotiz
    template_name = 'form.html'

    permission_required = 'nachrichten.add_nachricht'

    def form_valid(self, form):
        form.instance.notiz = True
        return super().form_valid(form)

class Nachricht(PermissionRequiredMixin, generic.DetailView):
    model = models.Nachricht

    template_name = 'nachricht.html'

    permission_required = 'nachrichten.view_nachricht'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['befoerderungsvermerk'] = forms.Befoerderungsvermerk()
        context['verteilungsvermerk'] = forms.Verteilungsvermerk()
        context['verteilungsvermerk'].fields['verteiler'].queryset = models.Funktion.objects.exclude(pk__in=self.object.verteilungsvermerke.all().values_list('verteiler', flat=True).distinct())
        context['verteiler'] = models.Funktion.objects.filter(pk__in=self.object.verteilungsvermerke.all().values_list('verteiler', flat=True).distinct())
        return context

class Annahmevermerk(PermissionRequiredMixin, generic.CreateView):
    model = models.Annahmevermerk
    permission_required = 'nachrichten.add_annahmevermerk'
    template_name = 'form.html'
    fields = []

    def get(self, request, *args, **kwargs):
        nachricht=models.Nachricht.objects.get(id=kwargs['pk'])
        return HttpResponseRedirect(nachricht.get_absolute_url())

    def form_valid(self, form):
        nachricht=models.Nachricht.objects.get(id=self.kwargs['pk'])
        models.Annahmevermerk.objects.get_or_create(
            nachricht=nachricht,
            benutzer=self.request.user
        )
        return HttpResponseRedirect(nachricht.get_absolute_url())

class Befoerderungsvermerk(PermissionRequiredMixin, generic.CreateView):
    model = models.Befoerderungsvermerk
    permission_required = 'nachrichten.add_befoerderungsvermerk'
    template_name = 'form.html'
    form_class = forms.Befoerderungsvermerk

    def get(self, request, *args, **kwargs):
        nachricht=models.Nachricht.objects.get(id=kwargs['pk'])
        return HttpResponseRedirect(nachricht.get_absolute_url())

    def form_valid(self, form):
        nachricht=models.Nachricht.objects.get(id=self.kwargs['pk'])
        models.Befoerderungsvermerk.objects.get_or_create(
            nachricht=nachricht,
            benutzer=self.request.user,
            weg=form.cleaned_data['weg'],
        )
        return HttpResponseRedirect(nachricht.get_absolute_url())

class Verteilungsvermerk(PermissionRequiredMixin, generic.CreateView):
    model = models.Verteilungsvermerk
    permission_required = 'nachrichten.add_verteilungsvermerk'
    template_name = 'form.html'
    form_class = forms.Verteilungsvermerk

    def get(self, request, *args, **kwargs):
        nachricht=models.Nachricht.objects.get(id=kwargs['pk'])
        return HttpResponseRedirect(nachricht.get_absolute_url())

    def get_form(self):
        form = super(Verteilungsvermerk, self).get_form(self.get_form_class())
        nachricht=models.Nachricht.objects.get(id=self.kwargs['pk'])
        form.fields['verteiler'].queryset = models.Funktion.objects.exclude(pk__in=nachricht.verteilungsvermerke.all().values_list('verteiler', flat=True).distinct())
        return form

    def form_valid(self, form):
        nachricht = models.Nachricht.objects.get(id=self.kwargs['pk'])
        form.instance.nachricht = nachricht
        form.instance.benutzer = self.request.user
        self.success_url = nachricht.get_absolute_url()
        return super().form_valid(form)

class Sichtungsvermerk(PermissionRequiredMixin, generic.CreateView):
    model = models.Sichtungsvermerk
    permission_required = 'nachrichten.add_sichtungsvermerk'
    template_name = 'form.html'
    fields = []

    # def get(self, request, *args, **kwargs):
    #     nachricht=models.Nachricht.objects.get(id=kwargs['pk'])
    #     return HttpResponseRedirect(nachricht.get_absolute_url())

    def form_valid(self, form):
        nachricht=models.Nachricht.objects.get(id=self.kwargs['pk'])
        models.Sichtungsvermerk.objects.get_or_create(
            nachricht=nachricht,
            benutzer=self.request.user
        )
        return HttpResponseRedirect(nachricht.get_absolute_url())


class Nachweisung(PermissionRequiredMixin, generic.ListView):

    model = models.Nachricht
    template_name = 'nachrichten.html'

    permission_required = 'nachrichten.view_nachricht'

    def get_context_data(self, **kwargs):
        context = super(Nachweisung, self).get_context_data(**kwargs)
        context.update({'title':'Nachweisung'})
        return context

class Ausgang(PermissionRequiredMixin, generic.ListView):

    model = models.Nachricht
    template_name = 'nachrichten.html'

    queryset = models.Nachricht.objects.filter(befoerderungsvermerk__isnull=True,richtung='A')

    permission_required = 'nachrichten.view_nachricht'

    def get_context_data(self, **kwargs):
        context = super(Ausgang, self).get_context_data(**kwargs)
        context.update({'title':'Ausgang'})
        return context
