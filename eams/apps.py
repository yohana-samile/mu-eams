from django.apps import AppConfig

class EamsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'eams'

    # fr prfl
    def ready(self):
        from . import signals
