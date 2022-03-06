from django.contrib.auth.models import User
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.views import APIView


# from django.contrib.auth.mixins import PermissionRequiredMixin

class ExampleView(APIView):
  permission_classes = (DjangoModelPermissions,)

  def get_queryset(self):
    return User.objects.all()

  # permission_required = ('poll.add_vote', 'poll.change_vote')
  def get(self, request, format=None):
    content = {
      'user': str(request.user),  # `django.contrib.auth.User` instance.
      'auth': str(request.auth),  # None
    }
    return Response(content)
