from django.shortcuts import render
from resource_db.models import LearningResource

# Making a function-based view to begin with, for testing purposes. 

def resource_list(request):
	resources = LearningResource.objects.all()

	return render(request, 'resource_db/resources.html', {'resources': resources})


