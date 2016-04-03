from django.contrib import admin

from .models import Subject
from .models import Office
from .models import FormConfig
from .models import FormField
from .models import FormLog


class SubjectAdmin(admin.ModelAdmin):
	list_display = ['subject', 'email', 'phone', 'from_name', 'from_email']
	search_fields = ['subject', 'email', 'phone', 'from_name', 'from_email']
	ordering = ['subject']

admin.site.register(Subject, SubjectAdmin)


class OfficeAdmin(admin.ModelAdmin):
	list_display = ['name', 'phone', 'email', 'address', 'www']
	search_fields = ['name', 'description', 'phone', 'email', 'address', 'www']
	list_filter = ['public', 'main', 'sites']
	ordering = ['name']

admin.site.register(Office, OfficeAdmin)


class FormFieldInline(admin.StackedInline):
	model = FormField
	extra = 1
	fields = ['label', 'help_text', 'name', 'field_type', 'required', 'choices', 'default', 'placeholder', 'order']

class FormConfigAdmin(admin.ModelAdmin):
	list_display = ['title']
	ordering = ['title']
	inlines = [FormFieldInline]

admin.site.register(FormConfig, FormConfigAdmin)

admin.site.register(FormLog)
