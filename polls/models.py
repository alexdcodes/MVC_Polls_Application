import datetime

from django.db import models
from django.utils import timezone


class Poll(models.Model):
    nickname = models.CharField(max_length=50)
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date pushed')

    def __unicode__(self):
        return self.question

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date < now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Pushed recently?'


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)

    @property
    def votes(self):
        return len(self.vote_set.all())

    def __unicode__(self):
        return self.choice_text


class Vote(models.Model):
    choice = models.ForeignKey(Choice)
    comment = models.TextField()

