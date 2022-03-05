import montrafic.views as views
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
  path('signin/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('signin/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('signup/', views.RegisterView.as_view(), name='auth_register'),

  path('', views.ExampleView.as_view(), name='signup'),

]
