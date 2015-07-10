from django.forms import ModelForm

from .models import Message


class MessageForm(ModelForm):

	class Meta:
		model = Message
		exclude = ['created_at', 'ip']
