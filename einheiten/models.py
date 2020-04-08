from django.db import models

class Einheit(models.Model):

    name = models.CharField(max_length=200)
    taktisches_zeichen = models.ImageField(verbose_name="Taktisches Zeichen", upload_to='einheiten/taktisches_zeichen/',blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Einheit"
        verbose_name_plural = "Einheiten"
