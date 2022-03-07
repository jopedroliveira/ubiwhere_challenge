from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from ..models import Segment
# class TraficSerializer(serializers.Serializer):
#   segment = SegmentSerializer()
#   intensity = serializers.CharField()
#   characterization = serializers.CharField()

class SegmentSerializer(serializers.ModelSerializer):
  intensity = serializers.SerializerMethodField()

  @classmethod
  def get_intensity(self, obj):
    return "cooool"

  class Meta:
    model = Segment
    read_only_fields = ("intensity",)
    fields = ["id", "latitude", "longitude", "length", "intensity"]