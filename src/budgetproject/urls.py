from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from core import urls

urlpatterns = [
    path("", include("core.urls")),
    path("admin/", admin.site.urls),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]

