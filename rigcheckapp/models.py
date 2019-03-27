from django.db import models


class Task(models.Model):
    complete = models.BooleanField()
    shift = models.ForeignKey("Shift", on_delete=models.CASCADE)
    station = models.ForeignKey("Station", on_delete=models.CASCADE)
    day = models.ForeignKey("Day", on_delete=models.CASCADE)
    sheet = models.ForeignKey("Sheet", on_delete=models.CASCADE)


class Shift(models.Model):
    shiftLetter = models.CharField(max_length=5)


class Station(models.Model):
    stationName = models.CharField(max_length=50)
    shift = models.ManyToManyField("Shift")
    day = models.ManyToManyField("Day")


class Day(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    shift = models.ForeignKey("Shift", on_delete=models.CASCADE)


class Sheet(models.Model):
    taskName = models.CharField(max_length=50)
    taskText = models.TextField()


# users model
