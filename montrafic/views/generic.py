from django.contrib.auth.models import User
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from ..models import Segment
from ..serializers import SegmentSerializer
# from django.contrib.auth.mixins import PermissionRequiredMixin

class SegmentView(ListAPIView):
  permission_classes = (IsAuthenticated, DjangoModelPermissions,)
  # permission_required = ('segment.add_vote', 'poll.change_vote')
  queryset = Segment.objects.all()
  serializer_class = SegmentSerializer

  # def get(self, request, *args, **kwargs):
  #   queryset = Segment.objects.all()
  #   serializer = SegmentSerializer(instance=data)
  #   return Response(data=serializer.data)
  #
  # def post(self, request, *args, **kwargs):
  #
  #   pass
  #
  # def put(self, request, *args, **kwargs):
  #   pass
  #
  # def delete(self, request, *args, **kwargs):
  #   pass

