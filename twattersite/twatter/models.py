# -*- coding: utf-8 -*-
from django.db import models

MOOD_CHOICES = ('happy', 'plain', 'sad', 'rage')

class Twat(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=16)
    mood = models.CharField(max_length=16, choices=[(a,a) for a in MOOD_CHOICES])
    text = models.TextField()

    def __unicode__(self):
        return u'@%s (%s): %s' % (self.author, self.mood, self.text)
    
    class Meta:
        ordering = ['-date']
