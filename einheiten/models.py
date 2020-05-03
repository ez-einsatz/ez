from django.db import models

from fahrzeuge import models as fahrzeuge_models
from personal import models as personal_models

class Einheit(models.Model):

    name = models.CharField(max_length=200)
    taktisches_zeichen = models.ImageField(verbose_name="Taktisches Zeichen", upload_to='einheiten/taktisches_zeichen/',blank=True)

    untereinheiten = models.ManyToManyField('self')
    fahrzeuge = models.ManyToManyField(fahrzeuge_models.Fahrzeug)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Einheit"
        verbose_name_plural = "Einheiten"

class Position(models.Model):

    name = models.CharField(max_length=200)
    taktisches_zeichen = models.ImageField(verbose_name="Taktisches Zeichen", upload_to='einheiten/taktisches_zeichen/',blank=True)

    einheit = models.ForeignKey(Einheit,related_name='positionen',on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Position"
        verbose_name_plural = "Positionen"

class Besetzung(models.Model):

    person = models.ForeignKey(personal_models.Person,blank=True,null=True,on_delete=models.CASCADE)
    position = models.ForeignKey(Position,related_name='besetzungen',on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Besetzung"
        verbose_name_plural = "Besetzungen"
