from django.db import models

class Einheit(models.Model):

    name = models.CharField(max_length=200)
    taktisches_zeichen = models.FileField(upload_to='media/einheiten/taktisches_zeichen/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Einheit"
        verbose_name_plural = "Einheiten"
