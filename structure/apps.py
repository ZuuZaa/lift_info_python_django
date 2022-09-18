from django.apps import AppConfig


class StructureConfig(AppConfig):
    name = 'structure'
    verbose_name = "Struktur"

    def ready(self):
        import structure.translation