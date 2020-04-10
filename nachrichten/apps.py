from django.apps import AppConfig


class NachrichtenConfig(AppConfig):
    name = 'nachrichten'

    def ready(self):
        from . import signals
