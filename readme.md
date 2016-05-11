# Django-Contact
A simple contact form.

# About
Simple contact form app.

# Install
* Add to INSTALLED_APPS 'apps.contacts',
* Add to urls.py url(r'^contacts/', include('apps.contacts.urls')),
* Add to CONTEXT_PROCESSORS 'apps.contacts.context_processors.offices',
* manage.py migrare contacts

* manage.py collectstatic
* Add this line to you head block

```html
<link rel='stylesheet' href='/static/contacts/css/all.css' type='text/css'>
```

# ToDo
* Add AJAX check views
* Notifer

* Check translations.py on firet multilanguage site
* https://github.com/stephenmcd/django-forms-builder/



# from django.core.mail import get_connection
from helpful.easy_email import mail


import urllib
import urllib2



def urlencode(string):
	string = urllib.unquote(string)
	string = u'' + urllib.quote(string.encode('utf-8'))
	return string


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
