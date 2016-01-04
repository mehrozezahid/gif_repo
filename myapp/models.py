from django.db import models


# Create your models here.


class Country(models.Model):
    country = models.CharField(max_length=30, unique=True)

    def __unicode__(self):
        return self.country


class League(models.Model):
    league = models.CharField(max_length=100, unique=True)
    country = models.ForeignKey(Country)

    def __unicode__(self):
        return self.league


class Match(models.Model):
    league = models.ForeignKey(League)
    home_team = models.CharField(max_length=50)
    away_team = models.CharField(max_length=50)
    home_team_score = models.IntegerField()
    away_team_score = models.IntegerField()
    time = models.DateTimeField()

    def __unicode__(self):
        return "{home_team} {home_team_score} - " \
               "{away_team_score} {away_team}".format(home_team=self.home_team,
                                                      home_team_score=self.home_team_score,
                                                      away_team_score=self.away_team_score,
                                                      away_team=self.away_team)


class Gif(models.Model):
    gif = models.TextField(max_length=300)
    match = models.ForeignKey(Match)

    def __unicode__(self):
        return self.gif
