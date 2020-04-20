from django.db import models
import nachrichten

class Einsatztagebucheintrag(models.Model):

    nachricht = models.OneToOneField(nachrichten.models.Nachricht,on_delete=models.CASCADE,null=True)

    information = models.TextField(null=True,blank=True)
    massnahme = models.TextField(null=True,blank=True)

    def get_absolute_url(self):
        return "/einsatztagebuch/eintrag/%i" % self.id

    class Meta:
        verbose_name = "Einsatztagebucheintrag"
        verbose_name_plural = "Einsatztagebucheinträge"
