from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('applications.user.urls')),
    path('booking/', include('applications.booking.urls')),
]