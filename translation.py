from modeltranslation.translator import translator
from modeltranslation.translator import TranslationOptions

from .models import Office


class OfficeTranslationOptions(TranslationOptions):
	fields = ['name', 'description', 'orgdata', 'address', 'www']

translator.register(Office, OfficeTranslationOptions)


# class FormConfigTranslationOptions(TranslationOptions):
# 	fields = ['title', 'submit_name', 'phone_placeholder', 'email_placeholder', 'comment_placeholder', 'error_message', 'tnx_message']

# translator.register(FormConfig, FormConfigTranslationOptions)