from django.urls import path
from . import views


urlpatterns = [
	path('<slug:slug>/', views.send, name='contacts_send'),
	path('<slug:slug>/validate/', views.validate, name='contacts_validate'),
]

