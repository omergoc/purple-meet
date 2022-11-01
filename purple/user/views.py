from .throttles import RegisterThrottle
from .serializers import ChangePasswordSerializer
from .models import Account
from rest_framework.generics import RetrieveUpdateAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView
from .serializers import UserSerializer, RegisterSerializer
from rest_framework.views import APIView
from rest_framework import status
from .permissions import NotAuthenticated


class AccountView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = Account.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, id = self.request.user.id)
        return obj

    def perform_update(self, serializer):
        serializer.save(user = self.request.user) 


class UpdatePassowrd(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        return self.request.user

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        data = {
            'old_password': request.data['old_password'],
            'new_password': request.data['new_password']
        }
        serializer = ChangePasswordSerializer(data = data)

        if serializer.is_valid():
            print(serializer.data)
            old_password = serializer.data.get('old_password')
            if not self.object.check_password(old_password):
                return Response({'old_password':'wrong_password'}, status=status.HTTP_400_BAD_REQUEST)

            self.object.set_password(serializer.data.get('new_password'))
            self.object.save()
            return Response(status = status.HTTP_204_NO_CONTENT)
        
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        

class CreateAccountView(CreateAPIView):
    throttle_classes = [RegisterThrottle]
    model = Account.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [NotAuthenticated]