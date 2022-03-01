from rest_framework.generics import CreateAPIView
from core.api.serializers import SubscriberSerializer
from core.models import Subscriber



class SubscribeAPIView(CreateAPIView):
    serializer_class = SubscriberSerializer
    model = Subscriber
    