from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('djangoapp/', include('djangoapp.app_urls')),
    path('', RedirectView.as_view(url='/djangoapp/', permanent=False)),
]
