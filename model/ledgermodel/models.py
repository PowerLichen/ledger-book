from django.db import models

# Create your models here.
class Ledger(models.Model):
    amount = models.IntegerField()
    description = models.CharField(max_length=200, default="", blank=True)