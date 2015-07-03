#!/usr/bin/env python
from databases.models import Property
from django.db import IntegrityError


def add_property(property_context):

    try:
        property = Property.objects.create(
            adverties_id=property_context['adverties_id'],
            title=property_context.get('title'),
            property_url=property_context.get('property_url'),
            location=property_context.get('location'),
            description=property_context.get('description'),
            monthly_rent=int(property_context['monthly_rent']),
            property_type=property_context.get('property_type'),
            posted_on=property_context('posted_on'),
        )
        property.save()
    except IntegrityError:
        pass
    return
