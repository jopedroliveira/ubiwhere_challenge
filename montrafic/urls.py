from django.urls import path
from rest_framework_simplejwt.views import (
  TokenObtainPairView,
  TokenRefreshView,
)
from rest_framework import routers

import montrafic.views as views

router = routers.SimpleRouter()

router.register(r"segments", views.SegmentModelViewSet, basename="segment_mng")

urlpatterns = [
  # todo
  # path('', views.TraficView.as_view(), name='trafic'),

  path('signin/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('signin/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('signup/', views.RegisterView.as_view(), name='auth_register'),

  # path('segment/', views.SegmentView.as_view(), name='segments'), # post only
  # path('segment/<segment_id>/', views.SegmentView.as_view(), name='segment_details'),
] + router.urls
