from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Django admin
    path('toate-dar-admin/', admin.site.urls),
    # path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),

    # User management
    path('accounts/', include('allauth.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
    # local apps
    # path('accounts/', include('users.urls')),
    path('', include('adra.urls', namespace="adra")),

]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
