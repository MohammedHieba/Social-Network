from django.apps import AppConfig


class ProfileInfoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profile_info'

    def ready(self):
        import profile_info.signals
