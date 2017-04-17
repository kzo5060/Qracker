from __future__ import unicode_literals

from django.db import models

from datetime import datetime

from django.contrib.auth.models import User

from django.core.validators import MaxValueValidator, MinValueValidator

class Transaction(models.Model):
    # Transactions entity
    creation_time = models.DateTimeField()
    delivery_time = models.DateTimeField()
    pickup_loc = models.CharField(max_length=64)
    code_word = models.CharField(max_length=32)

    # Initiates and Delivers relationships
    initiates = models.ForeignKey(User, related_name='initiates')
    delivers = models.ForeignKey(User, related_name='delivers')

    # Feedback entity
    timeliness = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    friendliness = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    responsetime = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    text_feedback = models.CharField(max_length=140)

    def __str__(self):
        return id

    def __unicode__(self):
        return id
