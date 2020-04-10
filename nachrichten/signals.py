from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.db import transaction

from . import models

import requests


def call_webhook(message_card,webhook_url):
    requests.post(
        webhook_url,
        data=message_card.json_payload,
        headers={
            "Content-Type": "application/json; charset=utf-8"
        },
        timeout=2.50
    )

@receiver(post_save, sender=models.Nachricht, dispatch_uid="nachricht_send_sichtung_webhooks")
def nachricht_send_sichtung_webhooks(sender, instance, created, update_fields, **kwargs):

    nachricht = instance
    message_card = nachricht.message_card()

    if created:
        for webhook in models.MicrosoftTeamsWebhook.objects.filter(funktion__isnull=True):
            call_webhook(message_card,webhook.webhook_url)

@receiver(m2m_changed, sender=models.Nachricht.verteiler.through, dispatch_uid="nachricht_send_verteiler_webhooks")
def nachricht_send_verteiler_webhooks(sender, instance, action, pk_set, **kwargs):


    nachricht = instance
    message_card = nachricht.message_card()

    if action == 'post_add':
        for pk in pk_set:
            funktion = models.Funktion.objects.get(pk=pk)

            for webhook in models.MicrosoftTeamsWebhook.objects.filter(funktion=funktion):
                call_webhook(message_card,webhook.webhook_url)
