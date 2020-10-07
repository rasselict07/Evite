from django.db import models


# Create your models here.

class EventUser(models.Model):
    user_id = models.CharField(max_length=100)
    event_id = models.ForeignKey(
        to='eviteapi.Event',
        on_delete=models.SET_NULL,
        null=True
    )


def __str__(self):
    return self.user_id
