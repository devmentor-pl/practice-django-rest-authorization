from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import PayloadView


urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("payload/", PayloadView.as_view(), name="payload"),
]
