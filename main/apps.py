from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'main'
    verbose_name = "Kontakt"
    
    def ready(self):
        import main.translation