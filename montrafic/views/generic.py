from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet

from ..models import *
from ..serializers import SegmentSerializer, SpeedSerializer


# from django.contrib.auth.mixins import PermissionRequiredMixin


class SegmentModelViewSet(ModelViewSet):
  permission_classes = (DjangoModelPermissions,)
  serializer_class = SegmentSerializer

  def get_queryset(self):
    query = Segment.objects.all().order_by('id')

    intensity_filter = self.request.GET.get("intensity", None)
    filter = None

    if intensity_filter and intensity_filter in INTENSITY_CHARACTERIZATION.keys():
      if intensity_filter == '2':
        filter = {"speed__lte": HIGH_THRESHOLD}
      elif intensity_filter == '1':
        filter = {"speed__gt": HIGH_THRESHOLD, "speed__lte": LOW_THRESHOLD}
      else:
        filter = {"speed__gte": LOW_THRESHOLD}

    if filter:
      # todo: move this logic to serializer or proper method
      from django.db.models import Count, Max
      speed_query = Speed.objects.filter(**filter)
      duplicates = speed_query.values('segment').order_by().annotate(
        max_creation_date=Max('creation_date'), count_id=Count('id')).filter(
        count_id__gt=1)
      exclude_list = []
      for duplicate in duplicates:
        exclude_list.append(
          Speed.objects.filter(segment=duplicate['segment']).exclude(
            creation_date=duplicate['max_creation_date']).values_list('id',
                                                                      flat=True))
      speed_query = speed_query.exclude(id__in=exclude_list)
      query = query.filter(segment_speed__in=speed_query)

    return query


class SpeedModelViewSet(ModelViewSet):
  permission_classes = (DjangoModelPermissions,)
  serializer_class = SpeedSerializer

  def get_queryset(self):
    return Speed.objects.all().order_by('-creation_date')
