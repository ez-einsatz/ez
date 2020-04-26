from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from django.db.models import ManyToManyField

from . import models

class VerteilungsvermerkAdmin(admin.ModelAdmin):
    #inlines = (VerteilerInline,)
    formfield_overrides = {
        ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

admin.site.register(models.Funktion)
admin.site.register(models.MicrosoftTeamsWebhook)
admin.site.register(models.VerteilerMail)
admin.site.register(models.Nachricht)
admin.site.register(models.Annahmevermerk)
admin.site.register(models.Befoerderungsvermerk)
admin.site.register(models.Verteilungsvermerk,VerteilungsvermerkAdmin)
admin.site.register(models.Sichtungsvermerk)
