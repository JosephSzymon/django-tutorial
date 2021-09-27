from django.db import models

class Tank(models.Model):
    model_name = models.CharField(max_length=50)
    weight = models.IntegerField()
    caliber = models.CharField(max_length=10)
