
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("HouseBookingApp.urls")),
    path("client/", include("client.urls")),
    path("communication/", include("communications.urls"))
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
