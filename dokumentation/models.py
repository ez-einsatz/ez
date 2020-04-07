from django.db import models
#from django.contrib.auth.models import User

class Meldung(models.Model):
    MELDUNGSRICHTUNG = (
            (0, 'Eingang'),
            (1, 'Ausgang'),
            (2, 'Gesprächsnotiz'),
        )
    richtung = models.IntegerField(default=0,
            choices=MELDUNGSRICHTUNG)

    von = models.CharField(max_length=200)
    an = models.CharField(max_length=200)
    inhalt = models.TextField()

    def __str__(self):
        return self.inhalt

    class Meta:
        verbose_name_plural = "Meldungen"

class Signatur(models.Model):

    zeit = models.DateTimeField(auto_now_add=True, blank=True)
    #user = models.ForeignKey(User)

    def __str__(self):
        return self.zeit.strftime("%d%H%M")

    class Meta:
        verbose_name_plural = "Signaturen"
