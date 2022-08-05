from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# from django.views.generic import TemplateView

schema_view = get_schema_view(
    openapi.Info(
        title="Cats API",
        default_version="v1",
        description="Документация для приложения cats проекта Kittygram",
        # terms_of_service="URL страницы с пользовательским соглашением",
        contact=openapi.Contact(email="admin@kittygram.ru"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


schema_view = get_schema_view(
    openapi.Info(
        title="yamdb_final",
        default_version="v1",
        description="Документация для прил. api_yamdb проекта yamdb_final",
        # terms_of_service="URL страницы с пользовательским соглашением",
        contact=openapi.Contact(email="andre33_3@rambler.ru"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    url(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    url(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    url(
        r"^redoc/$",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]
