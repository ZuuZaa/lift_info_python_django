from modeltranslation.translator import register, TranslationOptions
from .models import Department, Staff

@register(Department)
class DepartmentTranslationOptions(TranslationOptions):
    fields = ('name', 'address')

@register(Staff)
class StaffTranslationOptions(TranslationOptions):
    fields = ('full_name', 'role')