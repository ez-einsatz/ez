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

    aufnahmesignatur = models.ForeignKey(Signatur, blank=True, null=True, on_delete=models.CASCADE,related_name="aufnahmesignaturen",related_query_name="aufnahmesignatur")
    annahmesignatur = models.ForeignKey(Signatur, blank=True, null=True, on_delete=models.CASCADE,related_name="annahmesignaturen",related_query_name="annahmesignatur")
    #sichtung = models.ForeignKey(Signatur, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.inhalt

    class Meta:
        verbose_name = "Nachricht"
        verbose_name_plural = "Nachrichten"
