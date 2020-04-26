from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.db import transaction

from . import models, config, tasks

from django_mailbox.signals import message_received


@receiver(post_save, sender=models.Nachricht, dispatch_uid="nachricht_send_sichtung_hooks")
def nachricht_send_sichtung_hooks(sender, instance, created, update_fields, **kwargs):

    nachricht = instance

    if created:
        tasks.nachricht_send_sichtung_hooks.delay(nachricht.id)

@receiver(m2m_changed, sender=models.Verteilungsvermerk.verteiler.through, dispatch_uid="verteilungsvermerk_send_verteiler_webhooks")
def verteilungsvermerk_send_verteiler_hooks(sender, instance, action, pk_set, **kwargs):

    if action == 'post_add':
        for funktion_pk in pk_set:
            tasks.verteilungsvermerk_send_verteiler_hooks.delay(instance.nachricht.id,funktion_pk)

@receiver(message_received)
def mail_in(sender, message, **args):
    print( "recieved a message titled %s from a mailbox named %s" % (message.subject, message.mailbox.name))
    nachricht = models.Nachricht.objects.create(
        mail = message,
        betreff = message.subject,
        inhalt = message.text,
        richtung = 'E',
        absender = message.from_header,
        anschrift = message.to_header,
    )
    vermerk = models.Aufnahmevermerk.objects.create(
        nachricht=nachricht,
        weg={y: x for x, y in config.MELDEWEGE}['Mail'],
        kanal=message.mailbox,
    )
