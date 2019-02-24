import json 
import requests

from django.conf import settings

from django.http import HttpResponse
from django.utils.translation import ugettext as _

from .models import FormConfig, FormLog
from .forms import FormConfigForm


def send(request, slug):
	context = {}

	form_config = FormConfig.objects.get(slug=slug)
	data = request.POST or None

	form_config_form = FormConfigForm(data=data, form_config=form_config)


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

	context['RECAPTCHA_SITEKEY'] = settings.RECAPTCHA_SITEKEY
	context['captcha_is_valid'] = captcha_is_valid


	if request.POST and form_config_form.is_valid():
		form_log = FormLog(
			form_config=form_config,
			ip=request.META.get('REMOTE_ADDR', None),
			referrer=request.META.get('HTTP_REFERER', None),
			data=json.dumps(form_config_form.cleaned_data)
		)
		form_log.save()
		context['status'] = 'sent'
	else:
		context['status'] = 'error'
		context['errors'] = form_config_form.errors

	return HttpResponse(json.dumps(context), content_type='application/json')


def validate(request, slug):
	context = {}

	form_config = FormConfig.objects.get(slug=slug)
	data = request.POST or None

	form_config_form = FormConfigForm(data=data, form_config=form_config)

	if request.POST and form_config_form.is_valid():
		context['errors'] = False
	else:
		context['errors'] = form_config_form.errors

	return HttpResponse(json.dumps(context), content_type='application/json')
