from __future__ import absolute_import, unicode_literals

from celery import shared_task

import requests
from django.core.mail import EmailMessage

from . import models, config, tasks

@shared_task
def send_mail(nachricht_pk,mail_address):

    nachricht = models.Nachricht.objects.get(id=nachricht_pk)
    print(nachricht,mail_address)

    email = EmailMessage(
        nachricht,
        nachricht.inhalt,
        mail_address,
        ['einsatzstab-test@drkdieburg.de'],
    )
    email.send()

@shared_task
def call_microsoft_teams_webhook(nachricht_pk,webhook_url):

    nachricht = models.Nachricht.objects.get(id=nachricht_pk)

    message_card = nachricht.message_card()
    requests.post(
        webhook_url,
        data=message_card.json_payload,
        headers={
            "Content-Type": "application/json; charset=utf-8"
        },
        timeout=2.50
    )

@shared_task
def nachricht_send_sichtung_hooks(nachricht_pk):

    for vmail in models.VerteilerMail.objects.filter(funktion__isnull=True):
        tasks.send_mail.delay(nachricht_pk,vmail.mail_address)

    for webhook in models.MicrosoftTeamsWebhook.objects.filter(funktion__isnull=True):
        call_microsoft_teams_webhook.delay(nachricht_pk,webhook.webhook_url)

@shared_task
def verteilungsvermerk_send_verteiler_hooks(nachricht_pk,funktion_pk):

    for vmail in models.VerteilerMail.objects.filter(funktion_id=funktion_pk):
        tasks.send_mail.delay(nachricht_pk,vmail.mail_address)

    for webhook in models.MicrosoftTeamsWebhook.objects.filter(funktion_id=funktion_pk):
        tasks.call_microsoft_teams_webhook.delay(nachricht_pk,webhook.webhook_url)
