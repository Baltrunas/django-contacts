import json
from django.db import models

from django.utils.translation import ugettext_lazy as _

from django.contrib.sites.models import Site

from . import fields


class Office(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=128)
	description = models.TextField(verbose_name=_('Description'), blank=True, null=True)

	phone = models.CharField(verbose_name=_('Phone'), max_length=256, default='+7 (000) 000-00-00', blank=True, null=True)
	email = models.CharField(verbose_name=_('E-Mail'), max_length=128, default='email@mail.com', blank=True, null=True)
	www = models.URLField(verbose_name=_('WWW'), max_length=64, default='http://glav.it/', blank=True, null=True)
	photo = models.ImageField(verbose_name=_('Photo'), upload_to='img/office', blank=True)

	address_country = models.CharField(_('Country'), max_length=256, blank=True)
	address_locality = models.CharField(_('Locality'), help_text=_('Mountain View'), max_length=256, blank=True)
	address_region = models.CharField(_('Region'), help_text=_('CA'), max_length=256, blank=True)
	address_box = models.CharField(_('Post office box number'), help_text=_('The post office box number for PO box addresses'), max_length=256, blank=True)
	address_postal = models.CharField(_('Postal code'), max_length=256, blank=True)
	address_street = models.CharField(_('Street address'), help_text=_('T1600 Amphitheatre Pkwy'), max_length=256, blank=True)

	latitude = models.DecimalField(verbose_name=_('Latitude'), max_digits=19, decimal_places=15, blank=True, null=True)
	longitude = models.DecimalField(verbose_name=_('Longitude'), max_digits=19, decimal_places=15, blank=True, null=True)
	center_latitude = models.DecimalField(verbose_name=_('Center latitude'), max_digits=19, decimal_places=15, null=True, blank=True)
	center_longitude = models.DecimalField(verbose_name=_('Center longitude'), max_digits=19, decimal_places=15, null=True, blank=True)
	zoom = models.PositiveSmallIntegerField(verbose_name=_('Zoom'), null=True, blank=True, default=15)

	sites = models.ManyToManyField(Site, related_name='offices', verbose_name=_('Sites'))
	order = models.PositiveSmallIntegerField(verbose_name=_('Sort order'), default=500)
	main = models.BooleanField(verbose_name=_('Main'), default=True)

	public = models.BooleanField(verbose_name=_('Public'), default=True)
	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

	def address(self):
		return '%s, %s' % (self.address_region, self.address_street)

	def get_latitude(self):
		return '%s' % self.latitude

	def get_longitude(self):
		return '%s' % self.longitude

	def get_center_latitude(self):
		return '%s' % self.center_latitude

	def get_center_longitude(self):
		return '%s' % self.center_longitude

	def phones(self):
		return [phone.strip() for phone in self.phone.split(', ')]

	def __init__(self, *args, **kwargs):
		super(Office, self).__init__(*args, **kwargs)
		for feature in self.features.all():
			setattr(self, feature.key, feature.value)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['order', 'name']
		verbose_name = _('Office')
		verbose_name_plural = _('Offices')


class OfficeFeature(models.Model):
	office = models.ForeignKey(Office, verbose_name=_('Office'), related_name='features')
	name = models.CharField(_('Name'), max_length=128)
	key = models.SlugField(_('Key'), max_length=128)
	value = models.TextField(_('Value'), null=True, blank=True)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['office', 'name']
		verbose_name = _('Office feature')
		verbose_name_plural = _('Office features')


class FormConfig(models.Model):
	title = models.CharField(_('Title'), max_length=128)
	slug = models.SlugField(_('Slug'), max_length=128, unique=True)
	submit_name = models.CharField(_('Submit bottom name'), max_length=128)

	# error_message = models.TextField(_('Error Message'), blank=True, null=True)
	success_message = models.TextField(_('Success message'), blank=True)

	public = models.BooleanField(_('Public'), default=True)
	created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(_('Updated At'), auto_now=True)

	def __unicode__(self):
		return self.title

	@models.permalink
	def get_absolute_url(self):
		return ('contacts_ajax', (), {'slug': self.slug})

	class Meta:
		ordering = ['-created_at']
		verbose_name = _('Form config')
		verbose_name_plural = _('Forms configs')


class FormField(models.Model):
	form_config = models.ForeignKey(FormConfig, verbose_name=_('Form Config'), related_name='fields')

	label = models.CharField(_('Label'), max_length=128)
	help_text = models.CharField(_('Help text'), max_length=1024, null=True, blank=True)
	name = models.SlugField(_('Name'), max_length=100)

	field_type = models.IntegerField(_('Type'), choices=fields.NAMES)

	required = models.BooleanField(_('Required'), default=True)
	choices = models.TextField(_('Choices'), null=True, blank=True)
	default = models.CharField(_('Default'), max_length=1024, null=True, blank=True)
	placeholder = models.CharField(_('Placeholder'), max_length=1024, null=True, blank=True)
	order = models.IntegerField(verbose_name=_('Sort ordering'), default=500)

	def __unicode__(self):
		return self.name

	def get_choices(self):
		list_choices = []
		for choice in self.choices.split('\n'):
			list_choices.append((choice.split(': ')[0], choice.split(': ')[1]))
		print list_choices
		return list_choices

	class Meta:
		ordering = ['order']
		verbose_name = _('Field')
		verbose_name_plural = _('Fields')


class FormLog(models.Model):
	form_config = models.ForeignKey(FormConfig, verbose_name=_('Form Config'))
	ip = models.GenericIPAddressField(_('IP'), blank=True, null=True)
	referrer = models.CharField(_('Referrer'), max_length=2048, blank=True, null=True)
	data = models.TextField(_('Data'), blank=True, null=True)
	created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(_('Updated At'), auto_now=True)

	def __unicode__(self):
		return 'Request #%s from %s' % (self.pk, self.created_at)

	def fields(self):
		form_data = json.loads(self.data)
		data = []
		for key in form_data:
			field = {}
			field['key'] = key
			field['value'] = form_data[key]
			field['label'] = self.form_config.fields.get(name=key).label

			data.append(field)
		return data

	def __init__(self, *args, **kwargs):
		super(FormLog, self).__init__(*args, **kwargs)
		for field in self.fields():
			setattr(self, field['key'], field['value'])

	class Meta:
		ordering = ['-created_at']
		verbose_name = _('Form log')
		verbose_name_plural = _('Form logs')




class Subject(models.Model):
	subject = models.CharField(verbose_name=_('Subject'), max_length=512)
	email = models.CharField(verbose_name=_('E-Mail'), max_length=128)
	phone = models.CharField(verbose_name=_('Phone'), max_length=32)
	from_name = models.CharField(verbose_name=_('From name'), max_length=128, blank=True, null=True)
	from_email = models.EmailField(verbose_name=_('From E-Mail'), max_length=128)
	email_host = models.CharField(verbose_name=_('EMAIL HOST'), max_length=1024, blank=True, null=True)
	email_host_user = models.CharField(verbose_name=_('EMAIL HOST USER'), max_length=255, blank=True, null=True)
	email_host_password = models.CharField(verbose_name=_('EMAIL HOST PASSWORD'), max_length=255, blank=True, null=True)
	email_port = models.PositiveSmallIntegerField(verbose_name=_('EMAIL_PORT'), blank=True, null=True)
	email_use_tls = models.BooleanField(verbose_name=_('EMAIL_USE_TLS'), default=False)
	email_use_ssl = models.BooleanField(verbose_name=_('EMAIL_USE_SSL'), default=False)
	email_timeout = models.IntegerField(verbose_name=_('EMAIL_TIMEOUT'), default=None, blank=True, null=True)
	email_ssl_keyfile = models.CharField(verbose_name=_('EMAIL_SSL_KEYFILE'), max_length=1024, blank=True, null=True)
	email_ssl_certfile = models.CharField(verbose_name=_('EMAIL_SSL_CERTFILE'), max_length=1024, blank=True, null=True)

	class Meta:
		verbose_name = _('Subject')
		verbose_name_plural = _('Subjects')

	def __unicode__(self):
		return self.subject
