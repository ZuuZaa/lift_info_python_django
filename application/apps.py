from django.apps import AppConfig


class ApplicationConfig(AppConfig):
    name = 'application'
    verbose_name = "Elektron müraciət"

    def ready(self):
        import application.translation    
