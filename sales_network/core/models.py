from django.db import models


class QrCode(models.Model):
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)
