# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField


# Create your models here.
class feedback(models.Model):
    name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    number= models.IntegerField()
    neighbourhood = models.CharField(max_length =30)
    rating = models.IntegerField()
    comments = models.TextField()

    def __str__(self):
            return self.name
    class Meta:
        ordering = ['name']

COLOR_CHOICES = (
    ('Nairobi','Nairobi'),
    ('Kisumu', 'Kisumu'),
    ('Coast','Coast'),
    ('Nanyuki','Nanyuki'),
    ('Mombasa','Mombasa'),
)

MY_CHOICES2 = ((1, '1'),
               (2, '2'),
               (3, '3'),
               (4, '4'),
               (5, '5'))


class Post(models.Model):
    name = models.ForeignKey(User)
    phone = models.IntegerField()
    neighbourhood = models.CharField(max_length=6, choices=COLOR_CHOICES, default='green')
    rating = MultiSelectField(choices= MY_CHOICES2)
    comments = models.TextField(max_length=100)



   
