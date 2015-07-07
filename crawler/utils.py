#!/usr/bin/env python
from crawler.models import Property
from django.db import IntegrityError


def add_property(property_context):

    try:
        property = Property.objects.create(
            adverties_id=property_context['adverties_id'],
            title=property_context.get('title', None),
            property_url=property_context.get('property_url', None),
            location=property_context.get('location', None),
            description=property_context.get('description', None),
            monthly_rent=int(property_context['monthly_rent']),
            property_type=property_context.get('property_type', None),
            posted_on=property_context.get('posted_on', None),
        )
        property.save()
    except IntegrityError:
        pass
    return
