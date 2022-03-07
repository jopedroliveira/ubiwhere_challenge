from django.contrib.gis.db import models
from django.utils import timezone

class Segment(models.Model):
  longitude = models.PointField(blank=False, null=False)
  latitude = models.PointField(blank=False, null=False)
  length = models.DecimalField(max_digits=15, decimal_places=9)


class Speed(models.Model):
  segment = models.ForeignKey(Segment, related_name='segment_speed', on_delete=models.PROTECT)
  speed = models.DecimalField(max_digits=15, decimal_places=12)
  creation_date = models.DateTimeField(default=timezone.now, blank=False, null=False)
