from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from api.auth.serializers import UserCreateSerializer
from model.usermodel.models import User


class CreateUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]
