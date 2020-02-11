from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from .schema import schema
from graphene_django.views import GraphQLView

urlpatterns = [
    path("", include("core.urls")),
    path("admin/", admin.site.urls),
    path("graphql/", GraphQLView.as_view(graphiql=True, schema=schema)),
]


if settings.DEBUG or settings.TESTING_MODE:
    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
