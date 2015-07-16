# Django-Contact
A simple contact form.

# About
Simple contact form app.

# Install
* Add to INSTALLED_APPS 'apps.contacts',
* Add to urls.py url(r'^contacts/', include('apps.contacts.urls')),
* manage.py syncdb
* manage.py collectstatic
* Add this line to you head block

```html
<link rel='stylesheet' href='/static/css/contacts.css' type='text/css'>
```

## object_dict
```
{% load object_dict %}
{% for field in message|object_dict %}
	{{ field.verbose_name }}
	{{ field.display }}
{% endfor %}
```

## abs_puth
```
{% load abs_puth %}
{% abs_puth "static" "templates/e-mail/css/style.css" %}
{% abs_puth "media" "templates/e-mail/css/style.css" %}
{% abs_puth "base" "templates/e-mail/css/style.css" %}
{% abs_puth "parent" "templates/e-mail/css/style.css" %}
```

## easy_email
template must be 'email/contacts'
files 'email/contacts.html' and 'email/contacts.txt'
must will exist
```
from apps.useful.easy_email import mail
mail(subject, context, template, from_email, to_email, connection=None)
```