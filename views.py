from django.shortcuts import render

from django.utils.translation import ugettext as _

from django.core.mail import get_connection, send_mail

from .forms import MessageForm

from .models import Office


def contacts(request):
	context = {}
	context['title'] = _('Contacts')
	host = request.META.get('HTTP_HOST')
	context['offices'] = Office.objects.filter(public=True, sites__domain__in=[host])

	context['form'] = MessageForm(request.POST or None)
	if context['form'].is_valid():
		message = context['form'].save()
		message.ip = context['ip'] = request.META.get('REMOTE_ADDR', None)
		send_from = '%s <%s>' % (message.subject.from_name, message.subject.from_email)
		try:
			connection = get_connection()
			connection.host = message.subject.email_host
			connection.port = message.subject.email_port
			connection.username = message.subject.email_host_user
			connection.password = message.subject.email_host_password
			connection.use_tls = message.subject.email_use_tls
			connection.use_ssl = message.subject.email_use_ssl
			connection.use_timeout = message.subject.email_timeout
			connection.ssl_keyfile = message.subject.email_ssl_keyfile
			connection.ssl_certfile = message.subject.email_ssl_certfile

			msg = 'From: %s\nE-Mail: %s\nPhone: %s\nSubject: %s\n\n %s' % (
				message.name,
				message.email,
				message.phone,
				message.subject,
				message.message
			)
			send_mail(message.subject.subject, msg, send_from, [message.subject.email], connection=connection)
		except:
			pass
		context['ok'] = True
		context['form'] = MessageForm()
	else:
		context['ok'] = False

	return render(request, 'contacts/page.html', context)
