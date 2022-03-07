from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import (
  TokenObtainPairView,
  TokenRefreshView,
)

import montrafic.views as views

router = routers.SimpleRouter()
router.register(r"segments", views.SegmentModelViewSet, basename="segment")
router.register(r"speeds", views.SpeedModelViewSet, basename="speed")

urlpatterns = [
                path('signin/', TokenObtainPairView.as_view(),
                     name='token_obtain_pair'),
                path('signin/refresh/', TokenRefreshView.as_view(),
                     name='token_refresh'),
                path('signup/', views.RegisterView.as_view(),
                     name='auth_register'),
              ] + router.urls
