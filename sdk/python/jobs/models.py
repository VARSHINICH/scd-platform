from django.db import models
from scd_sdk.manager import SCDManager

class Job(models.Model):
    id = models.CharField(max_length=64)
    version = models.IntegerField()
    uid = models.CharField(max_length=64, primary_key=True)
    status = models.CharField(max_length=32)
    rate = models.FloatField()
    company_id = models.CharField(max_length=64)
    contractor_id = models.CharField(max_length=64)

    objects = SCDManager()

    class Meta:
        unique_together = ('id', 'version')