from django.db import models


PROPERTY_TYPE = (
    ('1', 'RK'),
    ('2', '1 BHK'),
    ('3', '2 BHK'),
    ('4', '3 BHK'),
    ('5', '4 BHK')
    )


class Property(models.Model):
    """
    This class creates attributes for property.
    """
    adverties_id = models.CharField(
        blank=True,
        max_length=150,
        unique=True,
        null=True
    )
    title = models.CharField(
        blank=True,
        max_length=100,
        null=True
    )
    property_url = models.URLField(
        blank=True,
        max_length=200,
        null=True
    )
    location = models.CharField(
        choices=PROPERTY_TYPE,
        blank=True,
        max_length=250,
        null=True
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    monthly_rent = models.IntegerField(
        blank=True,
        null=True
    )
    property_type = models.CharField(
        blank=True,
        max_length=50,
        null=True
    )
    posted_on = models.DateField(
        blank=True,
        null=True
    )

    def __unicode__(self):
        return self.title
