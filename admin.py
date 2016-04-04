from django.contrib import admin

from .models import Subject
from .models import Office

from .models import OfficeFeature
from .models import FormConfig
from .models import FormField
from .models import FormLog

class SubjectAdmin(admin.ModelAdmin):
	list_display = ['subject', 'email', 'phone', 'from_name', 'from_email']
	search_fields = ['subject', 'email', 'phone', 'from_name', 'from_email']
	ordering = ['subject']

admin.site.register(Subject, SubjectAdmin)



class FormFieldInline(admin.StackedInline):
	model = FormField
	extra = 3


class FormConfigAdmin(admin.ModelAdmin):
	list_display = ['title', 'created_at']
	search_fields = ['title', 'created_at']
	ordering = ['title']

	inlines = [FormFieldInline]

admin.site.register(FormConfig, FormConfigAdmin)


class OfficeFeatureInline(admin.TabularInline):
	model = OfficeFeature
	extra = 3


class OfficeAdmin(admin.ModelAdmin):
	list_display = ['name', 'phone', 'email', 'address', 'www']
	search_fields = ['name', 'description', 'phone', 'email', 'address', 'www']
	list_filter = ['public', 'main', 'sites']
	ordering = ['name']
	inlines = [OfficeFeatureInline]

admin.site.register(Office, OfficeAdmin)


class FormLogAdmin(admin.ModelAdmin):
	list_display = ['form_config', 'referrer', 'created_at']
	search_fields = ['form_config', 'referrer', 'created_at']
	list_filter = ['form_config', 'referrer']

admin.site.register(FormLog, FormLogAdmin)
