from django.conf import settings
from django.db import models

# Create your models here.
class Ledger(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.IntegerField()
    description = models.CharField(max_length=200, default="", blank=True)
    create_date = models.DateField(auto_now_add=True)