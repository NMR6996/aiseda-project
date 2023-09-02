from django.db import models


# Create your models here.

class Team(models.Model):
    full_name = models.CharField(max_length=20)
    job = models.CharField(max_length=30)
    social_1 = models.CharField(max_length=50, null=True, blank=True)
    social_2 = models.CharField(max_length=50, null=True, blank=True)
    social_3 = models.CharField(max_length=50, null=True, blank=True)
    social_4 = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to="team/", null=True)
