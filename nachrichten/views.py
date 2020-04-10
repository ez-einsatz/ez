from django.shortcuts import render
from django.views import generic

from django.http import HttpResponse
from django.template import loader

from . import models

def index(request):
    nachrichten_liste = Nachricht.objects.all()
    template = loader.get_template('nachricht/index.html')
    context = {
        'nachrichten_liste': nachrichten_liste,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

class NachrichtCreate(generic.CreateView):
    model = models.Nachricht
    fields = ['inhalt','richtung']

class Nachweisung(generic.ListView):

    model = models.Nachricht
    #paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['now'] = timezone.now()
        return context
