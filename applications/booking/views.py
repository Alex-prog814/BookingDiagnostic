from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend

from applications.booking.models import BookingDiagnostic

from applications.booking.serializers import BookingDiagnosticSerializer


User = get_user_model()


class BookingDiagnosticCreateView(generics.CreateAPIView):
    model = BookingDiagnostic
    serializer_class = BookingDiagnosticSerializer
    permission_classes = [IsAuthenticated, ]

    def get_serializer_context(self):
        return {'request': self.request}


class BookingDiagnosticListView(generics.ListAPIView):
    queryset = BookingDiagnostic.objects.all()
    serializer_class = BookingDiagnosticSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date', 'master__email']
