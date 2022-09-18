from django.apps import AppConfig


class NewsConfig(AppConfig):
    name = 'news'
    verbose_name = "Xəbərlər"
    
    def ready(self):
        import news.translation