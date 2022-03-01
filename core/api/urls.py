from django.urls import path

from core.api.views import SubscribeAPIView

app_name = 'subscribe'

urlpatterns = [
    path("subscribe/", SubscribeAPIView.as_view(), name="subscribe")
]
