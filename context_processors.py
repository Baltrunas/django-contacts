from .models import Office


def offices(request):
	try:
		offices = Office.objects.filter(public=True, sites__id=request.site.id)
	except:
		offices = False
	return {'offices': offices}
