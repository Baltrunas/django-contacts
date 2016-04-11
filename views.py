# # -*- coding: utf-8 -*-
from django.http import HttpResponse

from django.utils.translation import ugettext as _

# from django.core.mail import get_connection

from .models import FormConfig, FormLog
# from .forms import FormLog

from helpful.easy_email import mail


import urllib
import urllib2


def urlencode(string):
	string = urllib.unquote(string)
	string = u'' + urllib.quote(string.encode('utf-8'))
	return string


def ajax(request, slug):
	context = {}

	form_config = FormConfig.objects.get(slug=slug)

	data = context['request'].POST or None
	form_config_form = FormConfigForm(data=data, form_config=form_config)

	if request.POST and form_config_form.is_valid():

		form_log = FormLog(
			form_config=form_config,
			ip=context['request'].META.get('REMOTE_ADDR', None),
			referrer=context['request'].META.get('HTTP_REFERER', None),
			data=json.dumps(form_config_form.cleaned_data)
		)
		form_log.save()


		# send_from = '%s <%s>' % (message.subject.from_name, message.subject.from_email)
		# try:
		# 	connection = get_connection()
		# 	connection.host = message.subject.email_host
		# 	connection.port = message.subject.email_port
		# 	connection.username = message.subject.email_host_user
		# 	connection.password = message.subject.email_host_password
		# 	connection.use_tls = message.subject.email_use_tls
		# 	connection.use_ssl = message.subject.email_use_ssl
		# 	connection.use_timeout = message.subject.email_timeout
		# 	connection.ssl_keyfile = message.subject.email_ssl_keyfile
		# 	connection.ssl_certfile = message.subject.email_ssl_certfile

		# 	context['message'] = message

		# 	mail(message.subject.subject, context, 'contacts/e-mail/message', send_from, [message.subject.email], connection=connection)
		# except:
		# 	pass

		# try:
		# 	text = u'Новая заявка!\n%s\n%s\n%s\n%s' % (new_request.name, new_request.phone, new_request.email, new_request.referrer)
		# 	if site_config.sms_name:
		# 		url = 'http://sms.ru/sms/send?api_id=%s&to=%s&text=%s&from=%s&translit=0' % (site_config.sms_key, urlencode(phone), urlencode(text), urlencode(site_config.sms_name))
		# 	else:
		# 		url = 'http://sms.ru/sms/send?api_id=%s&to=%s&text=%s&translit=0' % (site_config.sms_key, urlencode(phone), urlencode(text))
		# 	urllib2.urlopen(url)
		# except:
		# 	pass


		context['send'] = True
	else:
		context['errors'] = form_config_form.errors
		context['send'] = False

	return HttpResponse(json.dumps(context), content_type="application/json")
