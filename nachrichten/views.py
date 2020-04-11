from django.shortcuts import render
from django.views import generic

from django.http import HttpResponse
from django.template import loader

from . import models, forms

def index(request):
    nachrichten_liste = Nachricht.objects.all()
    template = loader.get_template('nachricht/index.html')
    context = {
        'nachrichten_liste': nachrichten_liste,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

class NeueEingehendeNachricht(generic.CreateView):
    model = models.Nachricht
    form_class = forms.NeueEingehendeNachricht
    template_name = 'form.html'

    def form_valid(self, form):
        form.instance.richtung = 'E'
        return super().form_valid(form)

class NeueAusgehendeNachricht(generic.CreateView):
    model = models.Nachricht
    form_class = forms.NeueAusgehendeNachricht
    template_name = 'form.html'

    def form_valid(self, form):
        form.instance.richtung = 'A'
        return super().form_valid(form)

class NeueNotiz(generic.CreateView):
    model = models.Nachricht
    form_class = forms.NeueNotiz
    template_name = 'form.html'

class Nachricht(generic.UpdateView):
    model = models.Nachricht
    form_class = forms.Nachricht
    template_name = 'nachricht.html'

class Nachweisung(generic.ListView):

    model = models.Nachricht
    template_name = 'nachweisung.html'

    #paginate_by = 100  # if pagination is desired

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     #context['now'] = timezone.now()
    #     return context
