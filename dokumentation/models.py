from django.db import models
#from django.contrib.auth.models import User

class Signatur(models.Model):

    zeit = models.DateTimeField(auto_now_add=True, blank=True)
    #user = models.ForeignKey(User)

    def __str__(self):
        return self.zeit.strftime("%d%H%M%b%-y").lower()

    class Meta:
        verbose_name = "Signatur"
        verbose_name_plural = "Signaturen"

class Nachricht(models.Model):
    MELDUNGSRICHTUNG = (
            (0, 'Eingang'),
            (1, 'Ausgang'),
        )
    richtung = models.IntegerField(default=0,
            choices=MELDUNGSRICHTUNG)

    notiz = models.BooleanField(default=False)

    absender = models.CharField(max_length=200)
    anschrift = models.CharField(max_length=200)
    inhalt = models.TextField()

    VORRANGSTUFEN = (
            (0, 'eee'),
            (1, 'sss'),
            (2, 'bbb'),
            (3, 'aaa'),
        )
    vorrangstufe = models.IntegerField(default=0, choices=VORRANGSTUFEN)

    MELDEWEGE = (
            (0, 'Fe'),
            (1, 'Fu'),
            (2, 'Me'),
            (3, 'Mail'),
            (4, 'SMS'),
            (5, 'Fax'),
            (6, 'MIS'),
        )
    aufnahmeweg = models.IntegerField(default=0, choices=MELDEWEGE)
    aufnahmevermerk = models.ForeignKey(Signatur, blank=True, null=True, on_delete=models.CASCADE,related_name="aufnahmevermerke",related_query_name="aufnahmevermerk")
    annahmevermerk = models.ForeignKey(Signatur, blank=True, null=True, on_delete=models.CASCADE,related_name="annahmevermerke",related_query_name="annahmevermerk")
    befoerderungsweg = models.IntegerField(default=0, choices=MELDEWEGE)
    befoerderungsvermerk = models.ForeignKey(Signatur, verbose_name="Beförderungsvermerk", blank=True, null=True, on_delete=models.CASCADE,related_name="befoerderungsvermerke",related_query_name="befoerderungsvermerk")

    def __str__(self):
        return self.inhalt

    class Meta:
        verbose_name = "Nachricht"
        verbose_name_plural = "Nachrichten"
