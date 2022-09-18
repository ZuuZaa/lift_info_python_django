from modeltranslation.translator import register, TranslationOptions
from .models import ApplicationSubject

@register(ApplicationSubject)
class ApplicationSubjectTranslationOptions(TranslationOptions):
    fields = ['name']