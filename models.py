from django.db import models

from django.utils.translation import ugettext_lazy as _

from django.contrib.sites.models import Site


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


class Message(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=100)
	email = models.EmailField(verbose_name=_('E-Mail'), max_length=50)
	phone = models.CharField(verbose_name=_('Phone'), max_length=32)
	subject = models.ForeignKey(Subject, related_name='messages', verbose_name=_('Subject'))
	message = models.TextField(verbose_name=_('Message'), blank=True)
	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
	ip = models.GenericIPAddressField(verbose_name=_('IP'), blank=True, null=True, editable=False)

	class Meta:
		verbose_name = _('Message')
		verbose_name_plural = _('Messages')

	def __unicode__(self):
		return self.name


class Office(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=128)
	description = models.TextField(verbose_name=_('Description'), blank=True, null=True)

	phone = models.CharField(verbose_name=_('Phone'), max_length=256, default='+7 (000) 000-00-00', blank=True, null=True)
	email = models.CharField(verbose_name=_('E-Mail'), max_length=128, default='email@mail.com', blank=True, null=True)
	address = models.CharField(verbose_name=_('Address'), max_length=2048, blank=True)

	www = models.URLField(verbose_name=_('WWW'), max_length=64, default='http://glav.it/', blank=True, null=True)
	photo = models.ImageField(verbose_name=_('Photo'), upload_to='img/office', blank=True)
	sites = models.ManyToManyField(Site, related_name='offices', verbose_name=_('Sites'))

	latitude = models.DecimalField(verbose_name=_('Latitude'), max_digits=19, decimal_places=15, blank=True, null=True)
	longitude = models.DecimalField(verbose_name=_('Longitude'), max_digits=19, decimal_places=15, blank=True, null=True)
	center_latitude = models.DecimalField(verbose_name=_('Center latitude'), max_digits=19, decimal_places=15, null=True, blank=True)
	center_longitude = models.DecimalField(verbose_name=_('Center longitude'), max_digits=19, decimal_places=15, null=True, blank=True)
	zoom = models.PositiveSmallIntegerField(verbose_name=_('Zoom'), null=True, blank=True, default=15)

	order = models.PositiveSmallIntegerField(verbose_name=_('Sort order'), default=500)
	main = models.BooleanField(verbose_name=_('Main'), default=True)

	public = models.BooleanField(verbose_name=_('Public'), default=True)
	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

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

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['order', 'name']
		verbose_name = _('Office')
		verbose_name_plural = _('Offices')


# Office from django-lp
# May-be add extra model for office extra data?
# class Office(models.Model):
	# orgdata = models.TextField(verbose_name=_('Organization Data'), blank=True, null=True)
	# skype = models.CharField(verbose_name=_('Skype'), max_length=128, blank=True, null=True)



# class Request(models.Model):
# 	config = models.ForeignKey('FormConfig', verbose_name=_('Form Config'), blank=True, null=True)
# 	site = models.ForeignKey(Site, verbose_name=_('Site'), blank=True, null=True)

# 	name = models.CharField(max_length=128, verbose_name=_('Name'))
# 	phone = models.CharField(max_length=32, verbose_name=_('Phone'), blank=True, null=True)
# 	email = models.EmailField(max_length=128, verbose_name=_('E-Mail'), blank=True, null=True)
# 	comment = models.TextField(verbose_name=_('Comment'), blank=True, null=True)

# 	ip = models.GenericIPAddressField(blank=True, null=True, editable=False, verbose_name=_('IP'))
# 	referrer = models.CharField(verbose_name=_('Referrer'), max_length=2048, blank=True, null=True, editable=False)

# 	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
# 	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

# 	def __unicode__(self):
# 		return 'Request #%s from %s' % (self.pk, self.name)

# 	class Meta:
# 		ordering = ['-created_at']
# 		verbose_name = _('Msg')
# 		verbose_name_plural = _('Msgs')


# class FormConfig(models.Model):
# 	title = models.CharField(max_length=128, verbose_name=_('Title'))
# 	show_title = models.BooleanField(verbose_name=_('Show form title'), default=False)
# 	submit_name = models.CharField(max_length=128, verbose_name=_('Submit bottom name'))

# 	phone = models.BooleanField(verbose_name=_('Show phone field'), default=True)
# 	phone_placeholder = models.CharField(max_length=128, verbose_name=_('Phone placeholder'), blank=True, null=True)

# 	email = models.BooleanField(verbose_name=_('Show e-mail field'), default=False)
# 	email_placeholder = models.CharField(max_length=128, verbose_name=_('E-Mail placeholder'), blank=True, null=True)

# 	comment = models.BooleanField(verbose_name=_('Show comment field'), default=False)
# 	comment_placeholder = models.CharField(max_length=128, verbose_name=_('Comment placeholder'), blank=True, null=True)

# 	error_message = models.TextField(verbose_name=_('Error Message'), blank=True, null=True)
# 	tnx_message = models.TextField(verbose_name=_('Tnx Message'), blank=True, null=True)

# 	public = models.BooleanField(verbose_name=_('Public'), default=True)
# 	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
# 	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)


# 	def get_form(self, initial=None):
# 		exclude_field = ['user', 'site', 'config']
# 		if not self.phone:
# 			exclude_field.append('phone')
# 			phone_field = False
# 		else:
# 			phone_field = forms.CharField(label=_('Phone'), max_length=200, widget=forms.TextInput(attrs={'required': 'required', 'placeholder': self.phone_placeholder}), required=True)

# 		if not self.email:
# 			exclude_field.append('email')
# 			email_field = False
# 		else:
# 			email_field = forms.EmailField(label=_('E-Mail'), max_length=200, widget=forms.TextInput(attrs={'type': 'email', 'required': 'required', 'placeholder': self.email_placeholder}), required=True)

# 		if not self.comment:
# 			exclude_field.append('comment')
# 			comment_field = False
# 		else:
# 			comment_field = forms.CharField(label=_('Comment'), widget=forms.Textarea(attrs={'placeholder': self.comment_placeholder}), required=True)

# 		config_field = forms.CharField(widget=forms.HiddenInput(), initial=self.id)

# 		class RequestForm(forms.ModelForm):
# 			config = config_field
# 			name = forms.CharField(label=_('Name'), max_length=200, widget=forms.TextInput(attrs={'required': 'required', 'placeholder': _('Name')}))

# 			if phone_field:
# 				phone = phone_field

# 			if email_field:
# 				email = email_field

# 			if comment_field:
# 				comment = comment_field

# 			class Meta:
# 				model = Request
# 				exclude = exclude_field

# 		return RequestForm(initial)

# 	@models.permalink
# 	def get_absolute_url(self):
# 		return ('request', (), {'id': self.id})

# 	def __unicode__(self):
# 		return self.title

# 	class Meta:
# 		ordering = ['-created_at']
# 		verbose_name = _('Form Config')
# 		verbose_name_plural = _('Forms Configs')

