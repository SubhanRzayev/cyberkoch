from rest_framework.generics import CreateAPIView
from core.api.serializers import EmailSerializer
from core.models import Subscriber



class EmailAPIView(CreateAPIView):
    serializer_class = EmailSerializer
    model = Subscriber