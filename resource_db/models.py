import csv
from django.db import models


class LearningResource(models.Model):
    url = models.URLField(max_length=2047)
    title = models.CharField(max_length=511)
    tags = models.CharField(max_length=511)
    description = models.TextField()
    cost = models.CharField(max_length=255)
    content_format = models.CharField(max_length=511, blank=True)


def importFromCSV(input_file):
    """Create LearningResources from a CSV file.

    Note: This does not save the results!

    :type input_file: file
    :rtype: list of LearningResource
    """
    reader = csv.reader(input_file)
    reader.next() # skip headers
    resources = []
    for record in reader:
        new_resource = LearningResource(
            url=record[0],
            title=record[1],
            tags=record[3],
            description=record[4],
            cost=record[5],
            content_format=record[9]
        )
        resources.append(new_resource)
    return resources
