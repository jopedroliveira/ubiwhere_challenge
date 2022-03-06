from django.contrib.gis.db import models


class Segment(models.Model):
  longitude = models.PointField(blank=False, null=False)
  latitude = models.PointField(blank=False, null=False)
  length = models.DecimalField(max_digits=15, decimal_places=9)
  speed = models.DecimalField(max_digits=15, decimal_places=12)
