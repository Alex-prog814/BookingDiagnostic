from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class BookingDiagnostic(models.Model):
    CHOICES = (
        ('10:00-11:00', '10:00-11:00'),
        ('11:00-12:00', '11:00-12:00'),
        ('12:00-13:00', '12:00-13:00'),
        ('13:00-14:00', '13:00-14:00'),
        ('14:00-15:00', '14:00-15:00'),
        ('15:00-16:00', '15:00-16:00'),
        ('16:00-17:00', '16:00-17:00'),
        ('17:00-18:00', '17:00-18:00'),
        ('18:00-19:00', '18:00-19:00'),
        ('19:00-20:00', '19:00-20:00')
    )
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booking_diagnostic_client')
    master = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booking_diagnostic_master')
    date = models.DateField()
    time = models.CharField(max_length=11, choices=CHOICES)

    def __str__(self):
        return f'{self.master.email} -> {self.date} -> {self.time}'
