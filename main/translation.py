from modeltranslation.translator import register, TranslationOptions
from .models import FooterLink, Contact

@register(FooterLink)
class FooterLinkTranslationOptions(TranslationOptions):
    fields = ['link_name']

@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = ['address']