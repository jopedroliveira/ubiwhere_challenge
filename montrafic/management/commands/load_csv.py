import csv

from django.contrib.gis.geos import Point
from django.core.management import BaseCommand
from django.utils import timezone

from montrafic.models import Segment


class Command(BaseCommand):
  help = "Loads street segment data from CSV file."

  def add_arguments(self, parser):
    parser.add_argument("file_path", type=str)

  def handle(self, *args, **options):
    start_time = timezone.now()
    file_path = options["file_path"]
    with open(file_path, "r") as csv_file:
      data = csv.reader(csv_file, delimiter=",")
      next(data)
      street_segments = []
      for row in data:
        segment = Segment(
          id=row[0],
          longitude=Point(float(row[1]), float(row[3])),
          latitude=Point(float(row[2]), float(row[4])),
          length=row[5],
          speed=row[6],
        )
        street_segments.append(segment)
        if len(street_segments) > 5000:
          Segment.objects.bulk_create(street_segments)
          street_segments = []
      if street_segments:
        Segment.objects.bulk_create(street_segments)
    end_time = timezone.now()
    self.stdout.write(
      self.style.SUCCESS(
        f"CSV successfully loaded. Total time: {(end_time - start_time).total_seconds()} seconds."
      )
    )
