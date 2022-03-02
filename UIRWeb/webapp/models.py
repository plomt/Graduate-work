from django.db import models


class Temperature(models.Model):
    fuel = models.IntegerField()
    termfuel = models.IntegerField()
    clad = models.IntegerField()
    tube = models.IntegerField()


class Pins(models.Model):
    pin1_void1 = models.FloatField()
    pin1_fuel = models.FloatField()
    pin1_void2 = models.FloatField()
    pin1_clad = models.FloatField()

    pin2_termfuel = models.FloatField()
    pin2_clad = models.FloatField()


class Zones(models.Model):
    zone1_x = models.FloatField()
    zone1_y = models.FloatField()
    zone1_d = models.FloatField()

    zone2_x = models.FloatField()
    zone2_y = models.FloatField()
    zone2_d = models.FloatField()

    zone3_x = models.FloatField()
    zone3_y = models.FloatField()
    zone3_d = models.FloatField()

    zone4_x = models.FloatField()
    zone4_y = models.FloatField()
    zone4_d = models.FloatField()


# Create your models here.
