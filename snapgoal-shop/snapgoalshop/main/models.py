from django.db import models
import uuid


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    price = models.IntegerField()
    image = models.URLField()
    category = models.CharField(max_length=255, blank=True, null=True)
    availability = models.BooleanField(default=True)
    feedback = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "product"

    def __str__(self):
        return self.title
