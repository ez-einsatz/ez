from django.db import models

class Fahrzeug(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Fahrzeug"
        verbose_name_plural = "Fahrzeuge"
