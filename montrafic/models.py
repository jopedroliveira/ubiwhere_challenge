from django.contrib.gis.db import models
from django.utils import timezone

INTENSITY_CHARACTERIZATION = {'0': "low", '1': "moderate", '2': "high"}
LOW_THRESHOLD = 50
HIGH_THRESHOLD = 20


class Segment(models.Model):
  longitude = models.PointField(blank=False, null=False)
  latitude = models.PointField(blank=False, null=False)
  length = models.DecimalField(max_digits=15, decimal_places=9)


class Speed(models.Model):
  segment = models.ForeignKey(Segment, related_name='segment_speed',
                              on_delete=models.PROTECT)
  speed = models.DecimalField(max_digits=15, decimal_places=12)
  creation_date = models.DateTimeField(default=timezone.now, blank=False,
                                       null=False)

  @property
  def intensity(self):
    if self.speed > LOW_THRESHOLD:
      return '0'
    elif self.speed > HIGH_THRESHOLD:
      return '1'
    return '2'

  @property
  def characterization(self):
    return INTENSITY_CHARACTERIZATION[self.intensity]
