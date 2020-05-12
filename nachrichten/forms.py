from django import forms
from . import models, config

class NeueEingehendeNachricht(forms.ModelForm):

    title = "Neue eingehende Nachricht"

    vorrangstufe = forms.ChoiceField(choices=config.VORRANGSTUFEN, widget=forms.RadioSelect(), initial='0')
    aufnahmeweg = forms.ChoiceField(choices=config.MELDEWEGE, widget=forms.RadioSelect())

    class Meta():
        model = models.Nachricht
        fields = ['aufnahmeweg','vorrangstufe','absender','inhalt']

class NeueAusgehendeNachricht(forms.ModelForm):

    title = "Neue ausgehende Nachricht"

    vorrangstufe = forms.ChoiceField(choices=config.VORRANGSTUFEN, widget=forms.RadioSelect(), initial='0')

    class Meta():
        model = models.Nachricht
        fields = ['vorrangstufe','anschrift','absender','inhalt']

class NeueMail(forms.ModelForm):

    title = "Neue ausgehende E-Mail"

    class Meta():
        model = models.Nachricht
        fields = ['betreff','inhalt']

class NeueNotiz(forms.ModelForm):

    title = "Neue Gesprächsnotiz"

    richtung = forms.ChoiceField(choices=config.MELDERICHTUNG, widget=forms.RadioSelect())
    vorrangstufe = forms.ChoiceField(choices=config.VORRANGSTUFEN, widget=forms.RadioSelect())

    class Meta():
        model = models.Nachricht
        fields = ['richtung','vorrangstufe','anschrift','absender','inhalt']

class Befoerderungsvermerk(forms.ModelForm):

    weg = forms.ChoiceField(
        choices=config.MELDEWEGE,
        widget=forms.RadioSelect(),
        label="Beförderungsvermerk",
    )

    class Meta():
        model = models.Befoerderungsvermerk
        fields = ['weg']

    def title(self):
        return self.instance

class Verteilungsvermerk(forms.ModelForm):

    verteiler = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=models.Funktion.objects.all(),
        label="verteilen an",
    )

    class Meta():
        model = models.Verteilungsvermerk
        fields = ['verteiler']

    title = "neuer Verteilungsvermerk"
