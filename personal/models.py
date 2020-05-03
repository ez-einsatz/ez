from django.db import models

class Person(models.Model):

    nachname = models.CharField(max_length=200)
    vorname = models.CharField(max_length=200)
    geburtsdatum = models.DateField()

    def __str__(self):
        return self.vorname + ' ' + self.nachname

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Personen"
