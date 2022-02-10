from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import action

from .models import UserProfile
from .permissions import IsUserProfileAuthor
from .serializers import RegisterSerializer, UserProfileSerializer


class RegistrationView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Successfully signed up', status=status.HTTP_201_CREATED)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, ]

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            permissions = [IsUserProfileAuthor, ]
        else:
            permissions = [IsAuthenticated, ]
        return [permission() for permission in permissions]

    def get_serializer_context(self):
        return {'request': self.request}

    @action(detail=False, methods=['get'])
    def own(self, request, pk=None):
        queryset = self.get_queryset()
        queryset = queryset.get(user=request.user)
        serializer = UserProfileSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
