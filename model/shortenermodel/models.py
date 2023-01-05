from django.db import models
from django.utils import timezone
from django.utils.crypto import get_random_string


def generate_short_id():
    return get_random_string(Shortener.CODE_LENGTH)


def default_time():
    return timezone.now() + timezone.timedelta(1)


class Shortener(models.Model):
    CODE_LENGTH = 7

    ledger = models.ForeignKey(
        'ledgermodel.Ledger', on_delete=models.CASCADE)
    code = models.CharField(max_length=CODE_LENGTH,
                            editable=False,
                            unique=True,
                            default=generate_short_id)
    expired_dt = models.DateTimeField(default=default_time)

    class Meta:
        db_table = 'short_url'
