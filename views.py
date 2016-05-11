import json 

from django.http import HttpResponse
from django.utils.translation import ugettext as _

from .models import FormConfig, FormLog
from .forms import FormConfigForm


def ajax(request, slug):
	context = {}

	form_config = FormConfig.objects.get(slug=slug)
	data = request.POST or None

	form_config_form = FormConfigForm(data=data, form_config=form_config)

	if request.POST and form_config_form.is_valid():
		form_log = FormLog(
			form_config=form_config,
			ip=request.META.get('REMOTE_ADDR', None),
			referrer=request.META.get('HTTP_REFERER', None),
			data=json.dumps(form_config_form.cleaned_data)
		)
		form_log.save()
		context['send'] = True
	else:
		context['errors'] = form_config_form.errors
		context['send'] = False

	return HttpResponse(json.dumps(context), content_type='application/json')
