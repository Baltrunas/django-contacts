from django.forms import ModelForm, Form
from django import forms

from .models import FormConfig
from . import fields


class FormConfigForm(Form):

	def __init__(self, form_config, *args, **kwargs):
		initial = kwargs.pop('initial', {})

		super(FormConfigForm, self).__init__(*args, **kwargs)

		for field in form_config.fields.all():
			field_key = field.name
			field_class = fields.CLASSES[field.field_type]
			field_widget = fields.WIDGETS.get(field.field_type)
			field_args = {
				'label': field.label,
				'required': field.required,
				'help_text': field.help_text
			}

			arg_names = field_class.__init__.__code__.co_varnames
			# if 'max_length' in arg_names:
				# field_args['max_length'] = settings.FIELD_MAX_LENGTH

			# Choices
			if 'choices' in arg_names:
				choices = field.get_choices()
			# 	if (field.field_type == fields.SELECT and
			# 			field.default not in [c[0] for c in choices]):
			# 		choices.insert(0, ("", field.placeholder_text))
				field_args["choices"] = choices

			if field_widget is not None:
				field_args['widget'] = field_widget


			self.fields[field_key] = field_class(**field_args)

			if field.placeholder:
				self.fields[field_key].widget.attrs['placeholder'] = field.placeholder



# Forms FROM LP!
# from django import forms
# from django.utils.translation import ugettext_lazy as _

# from .models import TariffOrder


# class Html5EmailInput(forms.widgets.Input):
# 	input_type = 'email'

# class TariffOrderForm(forms.ModelForm):
# 	name = forms.CharField(label=_('Name'),max_length=200, widget=forms.TextInput(attrs={'required': 'required', 'placeholder': _('Name')}))
# 	phone = forms.CharField(label=_('Phone'), max_length=200, widget=forms.TextInput(attrs={'required': 'required', 'placeholder': _('Phone')}))
# 	email = forms.EmailField(label=_('E-Mail'), max_length=200, widget=Html5EmailInput(attrs={'required': 'required', 'placeholder': _('info@express-page.ru')}))

# 	class Meta:
# 		model = TariffOrder
# 		exclude = ['user', 'site', 'tariff', 'total_price']
