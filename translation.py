from modeltranslation.translator import translator
from modeltranslation.translator import TranslationOptions

from .models import Office


class OfficeTranslationOptions(TranslationOptions):
	fields = ['name', 'description', 'orgdata', 'address', 'www']

translator.register(Office, OfficeTranslationOptions)
