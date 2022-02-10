from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.BookingDiagnosticCreateView.as_view(), name='booking-create'),
    path('list/', views.BookingDiagnosticListView.as_view(), name='booking-list'),
]
