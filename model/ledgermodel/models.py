from django.conf import settings
from django.db import models


class Ledger(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    description = models.CharField(max_length=200, default="", blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'ledger'
