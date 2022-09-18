from django.apps import AppConfig

class AboutConfig(AppConfig):
    name = 'about'
    verbose_name = "Haqqımızda"

    def ready(self):
        import about.translation
