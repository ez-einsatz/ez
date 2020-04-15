from django.db import models
#from django.contrib.auth.models import User
from django.conf import settings
from . import config

from django_actionable_messages.message_card.actions import OpenUri, HttpPOST, ActionCard
from django_actionable_messages.message_card.cards import MessageCard
from django_actionable_messages.message_card.elements import Fact, ActionTarget
from django_actionable_messages.message_card.inputs import TextInput
from django_actionable_messages.message_card.sections import Section
from django_actionable_messages.message_card.utils import OSType

class Signatur(models.Model):

    zeit = models.DateTimeField(auto_now_add=True, blank=True)
    #user = models.ForeignKey(User)

    def __str__(self):
        return self.zeit.strftime("%d%H%M%b%-y").lower()

    class Meta:
        verbose_name = "Signatur"
        verbose_name_plural = "Signaturen"


class Funktion(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Funktion"
        verbose_name_plural = "Funktionen"


class Nachricht(models.Model):
    richtung = models.CharField(max_length=1, choices=config.MELDERICHTUNG)

    notiz = models.BooleanField(verbose_name="Gesprächsnotiz", default=False)

    absender = models.CharField(max_length=200)
    anschrift = models.CharField(max_length=200)
    inhalt = models.TextField()

    vorrangstufe = models.IntegerField(default=0, choices=config.VORRANGSTUFEN)

    aufnahmeweg = models.IntegerField(blank=True, null=True, choices=config.MELDEWEGE)
    aufnahmevermerk = models.ForeignKey(Signatur, blank=True, null=True, on_delete=models.CASCADE,related_name="aufnahmevermerke",related_query_name="aufnahmevermerk")
    annahmevermerk = models.ForeignKey(Signatur, blank=True, null=True, on_delete=models.CASCADE,related_name="annahmevermerke",related_query_name="annahmevermerk")
    befoerderungsweg = models.IntegerField(blank=True, null=True, choices=config.MELDEWEGE)
    befoerderungsvermerk = models.ForeignKey(Signatur, verbose_name="Beförderungsvermerk", blank=True, null=True, on_delete=models.CASCADE,related_name="befoerderungsvermerke",related_query_name="befoerderungsvermerk")

    verteiler = models.ManyToManyField(Funktion, blank=True)
    sichtungsvermerk = models.ForeignKey(Signatur, verbose_name="Sichtungsvermerk", blank=True, null=True, on_delete=models.CASCADE,related_name="sichtungssvermerke",related_query_name="sichtungssvermerk")

    def __str__(self):
        title = "Nachricht"
        if self.notiz:
            title = "Gesprächsnotiz"
        title += " " + self.get_richtung_display()
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
