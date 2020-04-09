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


class Funktion(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Funktion"
        verbose_name_plural = "Funktionen"


class Nachricht(models.Model):
    MELDERICHTUNG = (
            ('E', 'Eingang'),
            ('A', 'Ausgang'),
        )
    richtung = models.CharField(max_length=1, choices=MELDERICHTUNG)

    notiz = models.BooleanField(verbose_name="Gesprächsnotiz", default=False)

    absender = models.CharField(max_length=200)
    anschrift = models.CharField(max_length=200)
    inhalt = models.TextField()

    VORRANGSTUFEN = (
            (0, 'einfach'), #eee
            (1, 'sofort'), #sss
            (2, 'BLITZ'), #bbb
            #(3, 'STAATSNOT'), #aaa
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
    aufnahmeweg = models.IntegerField(blank=True, null=True, choices=MELDEWEGE)
    aufnahmevermerk = models.ForeignKey(Signatur, blank=True, null=True, on_delete=models.CASCADE,related_name="aufnahmevermerke",related_query_name="aufnahmevermerk")
    annahmevermerk = models.ForeignKey(Signatur, blank=True, null=True, on_delete=models.CASCADE,related_name="annahmevermerke",related_query_name="annahmevermerk")
    befoerderungsweg = models.IntegerField(blank=True, null=True, choices=MELDEWEGE)
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

    class Meta:
        verbose_name = "Nachricht"
        verbose_name_plural = "Nachrichten"
