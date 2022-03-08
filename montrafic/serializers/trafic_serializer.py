from rest_framework import serializers

from ..models import Segment, Speed


class SegmentSerializer(serializers.ModelSerializer):
  intensity = serializers.SerializerMethodField()
  characterization = serializers.SerializerMethodField()

  @classmethod
  def get_intensity(self, obj):
    try:
      speed = obj.segment_speed.order_by("-creation_date").last()
      return speed.intensity
    except Exception as e:
      print(e)
      return None

  @classmethod
  def get_characterization(self, obj):
    try:
      speed = obj.segment_speed.order_by("-creation_date").last()
      return speed.characterization
    except Exception as e:
      print(e)
      return None

  class Meta:
    model = Segment
    read_only_fields = ("intensity", "characterization")
    fields = ["id", "latitude", "longitude", "length", "intensity",
              "characterization"]


class SpeedSerializer(serializers.ModelSerializer):
  class Meta:
    model = Speed
    fields = ["id", "segment", "speed", "creation_date"]
