"""
URL configuration for zariya_jewellry project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.http import FileResponse, Http404
import os

# Admin Customization
admin.site.site_header = "ZARIYA_JEWELLRY ADMIN"
admin.site.site_title = "Luxury Jewellery Dashboard"
admin.site.index_title = "Welcome to Zariya Management"


def cors_media_serve(request, path, document_root=None):
    """Serve media files with CORS headers so Flutter VTO iframe can load images."""
    full_path = os.path.join(document_root, path)
    if not os.path.exists(full_path):
        raise Http404
    response = FileResponse(open(full_path, 'rb'))
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'GET, OPTIONS'
    response['Access-Control-Allow-Headers'] = 'Origin, Content-Type'
    response['Cross-Origin-Resource-Policy'] = 'cross-origin'
    return response


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('api/v1/', include('api.urls')),
]

if settings.DEBUG:
    # Use CORS-enabled media serving instead of default static()
    urlpatterns += [
        re_path(
            r'^media/(?P<path>.*)$',
            cors_media_serve,
            {'document_root': settings.MEDIA_ROOT},
        ),
    ]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
