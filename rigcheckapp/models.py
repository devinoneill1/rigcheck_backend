from django.db import models


class Task(models.Model):
    complete = models.BooleanField()
    group = models.ForeignKey("Group", on_delete=models.CASCADE)
    station = models.ForeignKey("Station", on_delete=models.CASCADE)
    day = models.ForeignKey("Day", on_delete=models.CASCADE)
    sheet = models.ForeignKey("Sheet", on_delete=models.CASCADE)


class Group(models.Model):
    groupLetter = models.CharField(max_length=5)


class Station(models.Model):
    stationName = models.CharField(max_length=50)
    group = models.ManyToManyField("Group")
    day = models.ManyToManyField("Day")


class Day(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    group = models.ForeignKey("Group", on_delete=models.CASCADE)
