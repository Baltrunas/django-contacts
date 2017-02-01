from modeltranslation.translator import translator
from modeltranslation.translator import TranslationOptions

from .models import Office, OfficeFeature, FormConfig, FormField


class OfficeTranslationOptions(TranslationOptions):
	fields = ['name', 'description', 'address_country', 'address_locality', 'address_region', 'address_box', 'address_postal', 'address_street']

translator.register(Office, OfficeTranslationOptions)


class OfficeFeatureTranslationOptions(TranslationOptions):
	fields = ['name', 'value']

translator.register(OfficeFeature, OfficeFeatureTranslationOptions)


class FormConfigTranslationOptions(TranslationOptions):
	fields = ['title', 'submit_name', 'success_message']

translator.register(FormConfig, FormConfigTranslationOptions)


class FormFieldTranslationOptions(TranslationOptions):
	fields = ['label', 'choices']

translator.register(FormField, FormFieldTranslationOptions)
