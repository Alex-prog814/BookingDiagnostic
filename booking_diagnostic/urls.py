from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls.static import static

from booking_diagnostic import settings

schema_view = get_swagger_view(title='Booking Diagnostic')

urlpatterns = [
    path('', schema_view),
    path('admin/', admin.site.urls),
    path('user/', include('applications.user.urls')),
    path('booking/', include('applications.booking.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
