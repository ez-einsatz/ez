from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from django.db.models import ManyToManyField

from . import models

admin.site.register(models.Signatur)
admin.site.register(models.Funktion)
admin.site.register(models.MicrosoftTeamsWebhook)

class NachrichtAdmin(admin.ModelAdmin):
    #inlines = (VerteilerInline,)
    formfield_overrides = {
        ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

admin.site.register(models.Nachricht,NachrichtAdmin)
