from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet

from ..models import *
from ..serializers import SegmentSerializer, SpeedSerializer


# from django.contrib.auth.mixins import PermissionRequiredMixin


class SegmentModelViewSet(ModelViewSet):
  permission_classes = (DjangoModelPermissions,)
  serializer_class = SegmentSerializer

  def get_queryset(self):
    intensity_filter = request.GET.get("intensity", None)
    filter = None
    # if intensity_filter and intensity_filter in INTENSITY_CHARACTERIZATION.keys():
    #   if intensity_filter == 2:
    #     filter = {"segment_speed__lte": HIGH_THRESHOLD}
    #   elif intensity_filter == 1:
    #     filter = {"segment_speed__gt": HIGH_THRESHOLD, "segment_speed__lte": LOW_THRESHOLD }
    #   else:
    #     filter = {"segment_speed__gte": LOW_THRESHOLD}

    return Segment.objects.filter(**filter).order_by('id')


class SpeedModelViewSet(ModelViewSet):
  permission_classes = (DjangoModelPermissions,)
  serializer_class = SpeedSerializer

  def get_queryset(self):
    return Speed.objects.all().order_by('-creation_date')
