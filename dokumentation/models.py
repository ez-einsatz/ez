from django.db import models

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
