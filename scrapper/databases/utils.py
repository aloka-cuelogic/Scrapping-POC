#!/usr/bin/env python
from databases.models import Property
from django.db import IntegrityError


def create_property(property_context):

    try:
        property = Property.objects.create(
            adverties_id=property_context['adverties_id'],
            title=property_context['title'],
            property_url=property_context['property_url'],
            location=property_context['location'],
            description=property_context['description'],
            monthly_rent=int(property_context['monthly_rent']),
            property_type=property_context['property_type'],
            posted_on=property_context['posted_on'],
        )
        property.save()
    except IntegrityError:
        pass
    return
