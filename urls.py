from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^(?P<slug>[-_\w]+)/$', views.ajax, name='contacts_ajax'),
]
