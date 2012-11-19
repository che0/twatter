# -*- coding: utf-8 -*-
from django.db import models

MOOD_CHOICES = [
    'happy', 'plain', 'sad', 'rage',
    'bitch-please', 'cereal-guy', 'challenge-accepted',
    'everything-went-better', 'fap-guy', 'forever-alone', 'freddie',
    'fuck-yea', 'happy-guy', 'le-sir', 'lol-guy', 'me-gusta',
    'mother-of-god', 'not-bad', 'nothing-to-do-here', 'okay', 'pffcht',
    'poker-face', 'ragegirl', 'serious', 'so-close', 'trollface',
    'true-story', 'whatever', 'you-dont-say', 'y-u-no', 'all-the-things'
]

class Twat(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=16)
    mood = models.CharField(max_length=64, choices=[(a,a) for a in MOOD_CHOICES])
    text = models.TextField()

    def __unicode__(self):
        return u'@%s (%s): %s' % (self.author, self.mood, self.text)
    
    class Meta:
        ordering = ['-date']
