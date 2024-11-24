from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    uuid = models.UUIDField(unique=True)
    price = models.IntegerField()
    image = models.URLField()
    category = models.CharField(max_length=255, blank=True, null=True)
    availability = models.BooleanField(default=True)
    feedback = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title
