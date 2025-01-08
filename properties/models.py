from django.db import models
from django.contrib.auth.models import User

class Property(models.Model):
    STATUS_CHOICES = [ ('available', 'Available'), ('sold', 'Sold')]
    property_id = models.AutoField(primary_key=True)
    # user field is set to null True and blank True to allow Anonymous user temporarily
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="properties", null=True, blank=True)
    location = models.CharField(max_length=255)
    price = models.FloatField()
    property_type = models.CharField(max_length=50)
    description = models.TextField()
    amenities = models.JSONField(default=list)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.property_type} in {self.location} ({self.status})"

