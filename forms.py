from django.forms import ModelForm

from .models import Message


class MessageForm(ModelForm):

	class Meta:
		model = Message
		exclude = ['created_at', 'ip']


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
