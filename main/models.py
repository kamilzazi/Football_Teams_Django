from django.db import models

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=128)
    country = models.CharField(max_length=128, null=True)
    year = models.IntegerField(null=True)
    description = models.TextField(default='Football team.')
    photo = models.ImageField(null=True, blank=True, upload_to='crest')

    def __str__(self):
        return f'{self.name} - {self.country}'


class Player(models.Model):
    name = models.CharField(default='', blank=True, max_length=128)
    surname = models.CharField(default='', blank=True, max_length=128)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Sponsor(models.Model):
    company = models.CharField(max_length=128)
    teams_sponsor = models.ManyToManyField(Team)

    def __str__(self):
        return self.company



