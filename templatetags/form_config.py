import json
from django import template

from ..models import FormConfig, FormLog

from ..forms import FormConfigForm


register = template.Library()


@register.simple_tag(takes_context=True)
def form_config(context, slug, tpl='contacts/form_reload.html'):
	form_config = FormConfig.objects.get(slug=slug)

	context['form_config'] = form_config
	data = context['request'].POST or None

	form_config_form = FormConfigForm(data=data, form_config=form_config)

	if form_config_form.is_valid():
		form_log = FormLog(
			form_config=form_config,
			ip=context['request'].META.get('REMOTE_ADDR', None),
			referrer=context['request'].META.get('HTTP_REFERER', None),
			data=json.dumps(form_config_form.cleaned_data)
		)
		form_log.save()
		form_config.send = True

	context['form_config_form'] = form_config_form

	t = template.loader.get_template(tpl)
	return t.render(template.Context(context))
