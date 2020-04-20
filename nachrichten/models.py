from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from . import config

from django_actionable_messages.message_card.actions import OpenUri, HttpPOST, ActionCard
from django_actionable_messages.message_card.cards import MessageCard
from django_actionable_messages.message_card.elements import Fact, ActionTarget
from django_actionable_messages.message_card.inputs import TextInput
from django_actionable_messages.message_card.sections import Section
from django_actionable_messages.message_card.utils import OSType

class Funktion(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Funktion"
        verbose_name_plural = "Funktionen"

class Nachricht(models.Model):
    richtung = models.CharField(max_length=1, choices=config.MELDERICHTUNG)

    absender = models.CharField(max_length=200)
    anschrift = models.CharField(max_length=200)
    inhalt = models.TextField()

    vorrangstufe = models.IntegerField(default=0, choices=config.VORRANGSTUFEN)

    def __str__(self):
        title = self.get_richtung_display()
        title += " #"+str(self.id)

        return title

    def message_card(self):
        message_card = MessageCard(title=str(self), summary=str(self),
                                   theme_color="666666")
        message_card.add_sections(
            Section(
                facts=[
                    Fact("Absender:", self.absender),
                    Fact("Anschrift:", self.anschrift),
                ],
            )
        )
        message_card.add_sections(
           Section(
               text=self.inhalt,
           )
        )
        message_card.add_actions([
            OpenUri(name="Anzeigen", targets=[
                ActionTarget(OSType.DEFAULT, settings.BASE_URL+self.get_absolute_url())
            ])
        ])
        return message_card

    def get_absolute_url(self):
        return "/nachrichten/%i" % self.id

    class Meta:
        verbose_name = "Nachricht"
        verbose_name_plural = "Nachrichten"

class Aufnahmevermerk(models.Model):

    zeit = models.DateTimeField(auto_now_add=True)
    benutzer = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    nachricht = models.OneToOneField(Nachricht,on_delete=models.CASCADE,primary_key=True)
    weg = models.IntegerField(null=True, choices=config.MELDEWEGE)

    def __str__(self):
        r = str(self.get_weg_display()) + ' '
        r += self.zeit.strftime("%d%H%M%b%-y").lower()
        if self.benutzer:
            r += ' '+str(self.benutzer)
        return r

    class Meta:
        verbose_name = "Aufnahmevermerk"
        verbose_name_plural = "Aufnahmevermerke"

class Annahmevermerk(models.Model):

    zeit = models.DateTimeField(auto_now_add=True)
    benutzer = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    nachricht = models.OneToOneField(Nachricht,on_delete=models.CASCADE,primary_key=True)

    def __str__(self):
        r = self.zeit.strftime("%d%H%M%b%-y").lower()
        if self.benutzer:
            r += ' '+str(self.benutzer)
        return r

    class Meta:
        verbose_name = "Annahmevermerk"
        verbose_name_plural = "Annahmevermerke"

class Befoerderungsvermerk(models.Model):

    zeit = models.DateTimeField(auto_now_add=True)
    benutzer = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    nachricht = models.OneToOneField(Nachricht,on_delete=models.CASCADE,primary_key=True)
    weg = models.IntegerField(null=True, choices=config.MELDEWEGE)

    def __str__(self):
        r = str(self.get_weg_display()) + ' '
        r += self.zeit.strftime("%d%H%M%b%-y").lower()
        if self.benutzer:
            r += ' '+str(self.benutzer)
        return r

    class Meta:
        verbose_name = "Beförderungsvermerk"
        verbose_name_plural = "Beförderungsvermerke"

class Sichtungsvermerk(models.Model):

    zeit = models.DateTimeField(auto_now_add=True)
    benutzer = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    nachricht = models.OneToOneField(Nachricht,on_delete=models.CASCADE,primary_key=True)

    def __str__(self):
        r = self.zeit.strftime("%d%H%M%b%-y").lower()
        if self.benutzer:
            r += ' '+str(self.benutzer)
        return r

    class Meta:
        verbose_name = "Sichtungsvermerk"
        verbose_name_plural = "Sichtungsvermerke"

class Verteilungsvermerk(models.Model):

    zeit = models.DateTimeField(auto_now_add=True)
    benutzer = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    nachricht = models.ForeignKey(Nachricht,on_delete=models.CASCADE,related_name='verteilungsvermerke',null=True)

    verteiler = models.ManyToManyField(Funktion)

    def __str__(self):
        r = ''
        for funktion in self.verteiler.all():
            r += str(funktion) + ' '
        r += self.zeit.strftime("%d%H%M%b%-y").lower()
        if self.benutzer:
            r += ' '+str(self.benutzer)
        return r

    class Meta:
        verbose_name = "Verteilungsvermerk"
        verbose_name_plural = "Verteilungsvermerke"

class MicrosoftTeamsWebhook(models.Model):

    funktion = models.ForeignKey(Funktion, verbose_name="Funktion", blank=True, null=True, on_delete=models.CASCADE,related_name="funktionen",related_query_name="funktion")
    webhook_url = models.CharField(max_length=200, verbose_name="Microsoft Teams Webhook URL")

    def __str__(self):
        if not self.funktion == None:
            return str(self.funktion)
        else:
            return "Sichtung"


    class Meta:
        verbose_name = "Microsoft Teams Webhook"
        verbose_name_plural = "Microsoft Teams Webhooks"
