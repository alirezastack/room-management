from django.db import models


class Room(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    is_booked = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']
