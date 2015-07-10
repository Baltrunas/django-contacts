from django.contrib import admin

from .models import Subject
from .models import Message
from .models import Office


class SubjectAdmin(admin.ModelAdmin):
	list_display = ['subject', 'email', 'phone', 'from_name', 'from_email']
	search_fields = ['subject', 'email', 'phone', 'from_name', 'from_email']
	ordering = ['subject']

admin.site.register(Subject, SubjectAdmin)


class MessageAdmin(admin.ModelAdmin):
	list_display = ['name', 'email', 'phone', 'subject', 'message', 'ip', 'created_at']
	search_fields = ['name', 'email', 'phone', 'subject', 'message', 'ip', 'created_at']
	ordering = ['name']

admin.site.register(Message, MessageAdmin)


class OfficeAdmin(admin.ModelAdmin):
	list_display = ['name', 'phone', 'email', 'address', 'www']
	search_fields = ['name', 'description', 'phone', 'email', 'address', 'www']
	list_filter = ['public', 'main', 'sites']
	ordering = ['name']

admin.site.register(Office, OfficeAdmin)
