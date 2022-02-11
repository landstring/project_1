from django.db import models

class Admins(models.Model):
    username = models.CharField(max_length=300)
    telegram_id = models.CharField(max_length=100)
    TYPE = [
        ('1', "buy_admin"),
        ('2', "booking_admin"),
        ('3', "resume_admin")
    ]
    type = models.CharField(choices=TYPE, max_length=1)
