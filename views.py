# # -*- coding: utf-8 -*-
# from django.shortcuts import render

# from django.utils.translation import ugettext as _

# from django.core.mail import get_connection

# from helpful.easy_email import mail

# from .forms import MessageForm
# from .models import Office


# def contacts(request):
# 	context = {}

# 	context['title'] = _('Contacts')
# 	host = request.META.get('HTTP_HOST')
# 	context['offices'] = Office.objects.filter(public=True, sites__domain__in=[host])

# 	context['form'] = MessageForm(request.POST or None)
# 	if context['form'].is_valid():
# 		message = context['form'].save()
# 		message.ip = context['ip'] = request.META.get('REMOTE_ADDR', None)
# 		send_from = '%s <%s>' % (message.subject.from_name, message.subject.from_email)
# 		try:
# 			connection = get_connection()
# 			connection.host = message.subject.email_host
# 			connection.port = message.subject.email_port
# 			connection.username = message.subject.email_host_user
# 			connection.password = message.subject.email_host_password
# 			connection.use_tls = message.subject.email_use_tls
# 			connection.use_ssl = message.subject.email_use_ssl
# 			connection.use_timeout = message.subject.email_timeout
# 			connection.ssl_keyfile = message.subject.email_ssl_keyfile
# 			connection.ssl_certfile = message.subject.email_ssl_certfile

# 			context['message'] = message

# 			mail(message.subject.subject, context, 'contacts/e-mail/message', send_from, [message.subject.email], connection=connection)
# 		except:
# 			pass
# 		context['ok'] = True
# 		context['form'] = MessageForm()
# 	else:
# 		context['ok'] = False

# 	return render(request, 'contacts/page.html', context)




# FROM LP!!!


# 
# import json

# import urllib
# import urllib2


# from django.http import HttpResponse

# from django.shortcuts import render

# from django.template.loader import render_to_string
# from django.template import RequestContext

# # from django.utils.translation import ugettext_lazy as _

# from django import forms

# from django.core.mail import EmailMultiAlternatives
# # from django.core.mail import EmailMessage


# from .forms import TariffOrderForm

# from .models import SiteConfig
# from .models import Tariff
# from .models import FormConfig


# def urlencode(string):
# 	string = urllib.unquote(string)
# 	string = u'' + urllib.quote(string.encode('utf-8'))
# 	return string


# def request(request, id):
# 	context = {}

# 	site_config = SiteConfig.objects.get(site=request.site)
# 	phone = site_config.phone

# 	config = FormConfig.objects.get(id=id)

# 	form = config.get_form(request.POST or None)

# 	if request.POST:
# 		if form.is_valid():
# 			new_request = form.save()
# 			new_request.referrer = request.META.get('HTTP_REFERER', None)
# 			new_request.ip = request.META.get('REMOTE_ADDR', None)
# 			new_request.site = request.site
# 			new_request.config = config
# 			new_request.save()

# 			try:
# 				if site_config.send_sms and site_config.sms_key:
# 					text = u'Новая заявка!\n%s\n%s\n%s\n%s' % (new_request.name, new_request.phone, new_request.email, new_request.referrer)
# 					if site_config.sms_name:
# 						url = 'http://sms.ru/sms/send?api_id=%s&to=%s&text=%s&from=%s&translit=0' % (site_config.sms_key, urlencode(phone), urlencode(text), urlencode(site_config.sms_name))
# 					else:
# 						url = 'http://sms.ru/sms/send?api_id=%s&to=%s&text=%s&translit=0' % (site_config.sms_key, urlencode(phone), urlencode(text))
# 					urllib2.urlopen(url)
# 			except:
# 				pass

# 			if site_config.send_email:
# 				try:
# 					email_context = {}
# 					email_context['title'] = config.title
# 					email_context['object'] = new_request
# 					admin_content = render_to_string('email/result.html', email_context, context_instance=RequestContext(request))
# 					sendmsg = EmailMultiAlternatives(email_context['title'], admin_content, site_config.email, [site_config.email])
# 					sendmsg.attach_alternative(admin_content, "text/html")
# 					sendmsg.send()
# 				except:
# 					pass


# 			context['send'] = True
# 		else:
# 			context['errors'] = form.errors
# 			context['send'] = False

# 		return HttpResponse(json.dumps(context), content_type="application/json")

# 	else:
# 		context['config'] = config
# 		context['form'] = form
# 		return render(request, 'lp/page_form.html', context)
