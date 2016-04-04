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
<link rel='stylesheet' href='/static/css/contacts.css' type='text/css'>
```

# ToDo
* Add AJAX check views
* Notifer

* Check translations.py on firet multilanguage site
* https://github.com/stephenmcd/django-forms-builder/