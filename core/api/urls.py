from django.urls import path

from core.api.views import *

app_name = 'email_api'

urlpatterns = [
    path("email/", EmailAPIView.as_view(), name="email")
]
