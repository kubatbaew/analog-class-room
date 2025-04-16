from core.admin import admin_panel
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include("apps.pages.urls")),
    path('', include("apps.groups.urls")),
    path('', include("apps.users.urls")),
    path('', include("apps.works.urls")),
    path('admin/', admin_panel.site.urls),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.IMAGES_URL, document_root=settings.IMAGES_ROOT)
