from django import forms
from . import models, config

class NeueEingehendeNachricht(forms.ModelForm):

    title = "Neue eingehende Nachricht"

    vorrangstufe = forms.ChoiceField(choices=config.VORRANGSTUFEN, widget=forms.RadioSelect())
    aufnahmeweg = forms.ChoiceField(choices=config.MELDEWEGE, widget=forms.RadioSelect())

    class Meta():
        model = models.Nachricht
        fields = ['aufnahmeweg','vorrangstufe','absender','inhalt']

class NeueAusgehendeNachricht(forms.ModelForm):

    title = "Neue ausgehende Nachricht"

    vorrangstufe = forms.ChoiceField(choices=config.VORRANGSTUFEN, widget=forms.RadioSelect())

    class Meta():
        model = models.Nachricht
        fields = ['vorrangstufe','anschrift','inhalt']

class NeueNotiz(forms.ModelForm):

    title = "Neue Gesprächsnotiz"

    richtung = forms.ChoiceField(choices=config.MELDERICHTUNG, widget=forms.RadioSelect())
    vorrangstufe = forms.ChoiceField(choices=config.VORRANGSTUFEN, widget=forms.RadioSelect())

    class Meta():
        model = models.Nachricht
        fields = ['richtung','vorrangstufe','anschrift','absender','inhalt']

class Nachricht(forms.ModelForm):

    def title(self):
        return self.instance

    verteiler = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=models.Funktion.objects.all(),
        required=False
    )

    aufnahmeweg = forms.ChoiceField(
        choices=config.MELDEWEGE,
        widget=forms.RadioSelect(),
        label="Aufnahmevermerk"
    )
    befoerderungsweg = forms.ChoiceField(
        choices=config.MELDEWEGE,
        widget=forms.RadioSelect(),
        label="Beförderungsvermerk"
    )

    class Meta():
        model = models.Nachricht
        fields = ['verteiler']
