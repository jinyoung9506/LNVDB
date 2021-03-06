from django.db import models

# Create your models here.
class Candidate(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=10)
    introduction = models.TextField()
    area = models.CharField(max_length=15)
    party_number = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Poll(models.Model):
    objects = models.Manager()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    area = models.CharField(max_length=15)

    def __str__(self):
        return self.area


class Choice(models.Model):
    objects = models.Manager()
    poll = models.ForeignKey(Poll, on_delete = models.CASCADE,)
    candidate = models.ForeignKey(Candidate, on_delete = models.CASCADE,)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.candidate.name
