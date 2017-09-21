from django.forms import ModelForm, Form
from django import forms

from .models import FormConfig
from . import fields


class FormConfigForm(Form):

	def __init__(self, form_config, *args, **kwargs):
		self.form_config = form_config
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

			# Choices
			if 'choices' in arg_names:
				choices = field.get_choices()
				field_args['choices'] = choices

			if field_widget is not None:
				field_args['widget'] = field_widget


			self.fields[field_key] = field_class(**field_args)

			if field.placeholder:
				self.fields[field_key].widget.attrs['placeholder'] = field.placeholder

	def groups(self):
		groups = []
		field_groups = self.form_config.fields.order_by('group').distinct().values_list('group', flat=True)
		for group in field_groups:
			fields = []
			for field_name in self.form_config.fields.filter(group=group):
				for ff in self.visible_fields():
					if ff.name == field_name.name:
						fields.append(ff)
			groups.append({
				'name': group,
				'fields': fields
			})

		return groups
