from .models import Office


def offices(request):
	offices = Office.objects.filter(public=True, sites__id__in=[request.site.id])
	return {'offices': offices}
