from django.db import models
from highneed import settings
import datetime
from django.utils import timezone
# Create your models here.
from django.contrib.auth import get_user_model


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Event(models.Model):
    pub_date = models.DateTimeField('Date: ')
    title = models.CharField(max_length=200)
    description = models.TextField() #NEW
    data = models.DateField() #Date of Event
    place = models.CharField(max_length=500)
    likes = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' | ' + str(self.data) + ' | ' + self.place


class Koszyk(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='koszyk')
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(
        verbose_name='quantity', default=0)
