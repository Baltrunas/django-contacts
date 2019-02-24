import json
import requests

from django.conf import settings

from django import template
from django.template.loader import render_to_string

from ..models import FormConfig, FormLog
from ..forms import FormConfigForm


register = template.Library()


@register.simple_tag(takes_context=True)
def form_config(context, slug, tpl='contacts/form.html'):
	tag_context = {}

	form_config = FormConfig.objects.get(slug=slug)

	data = context['request'].POST or None
	request = context['request']

	form_config_form = FormConfigForm(data=data, form_config=form_config)
	form_config.status = 'new'

	captcha_is_valid = False
	if 'g-recaptcha-response' in request.POST and request.POST['g-recaptcha-response']:
		url = 'https://www.google.com/recaptcha/api/siteverify'
		data = {
			'secret': settings.CAPTCHA_SECRET,
			'response': request.POST['g-recaptcha-response'],
		}
		response = requests.get(url, params=data)

		if response.status_code == 200:
			raw_results = response.json()
			print(raw_results)
			if raw_results['success']:
				captcha_is_valid = True

	tag_context['RECAPTCHA_SITEKEY'] = settings.RECAPTCHA_SITEKEY
	tag_context['captcha_is_valid'] = captcha_is_valid

	if form_config_form.is_valid():
		FormLog.objects.create(
			form_config=form_config,
			ip=context['request'].META.get('REMOTE_ADDR', None),
			referrer=context['request'].META.get('HTTP_REFERER', None),
			data=json.dumps(form_config_form.cleaned_data)
		)
		form_config_form = FormConfigForm(data=None, form_config=form_config)
		form_config.status = 'sent'
	elif form_config_form.errors:
		form_config.status = 'error'

	tag_context['form_config'] = form_config
	tag_context['form_config_form'] = form_config_form
	return render_to_string(tpl, tag_context, context['request'])


@register.filter(name='field_type')
def field_type(field):
	return field.field.widget.__class__.__name__
