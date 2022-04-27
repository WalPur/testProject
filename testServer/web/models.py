from django.db import models

# Create your models here.
class Tournament(models.Model):
    name = models.CharField(max=128)
    STATUS_CHOICES = [
        ("CREATED", 'Created'),
        ("ACCEPTED", 'Accepted'),
        ("FINISHED", 'Finished'),
        ("CANCELLED", 'Cancelled')
    ]
    status = models.CharField(choices=STATUS_CHOICES, default="CREATED")
    start_date = models.DateField()
    finish_date = models.DateField()
    description = models.TextField()
    TYPE_CHOICES = [
        ('LOCAL', 'Local'),
        ('REGION', 'Region'),
        ('RUSSIA', 'Russia'),
        ('WORLD', 'World'),
        ('ONLINE', 'Online')
    ]
    type = models.CharField(choices=TYPE_CHOICES)
    FORMAT_CHOICES = [
        ('PAIR', 'Pair'),
        ('TEAM', 'Team'),
        ('INDIVIDDUAL', 'Individual')
    ]
    format = models.CharField(choices=FORMAT_CHOICES)