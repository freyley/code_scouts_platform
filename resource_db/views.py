from django.shortcuts import render
from resource_db.models import LearningResource
from lib.decorators import template

# Making a function-based view to begin with, for testing purposes.
@template("resource_db/resources.html")
def resource_list(request):
    resources = LearningResource.objects.all()
    return dict(
            resources=resources
        )
