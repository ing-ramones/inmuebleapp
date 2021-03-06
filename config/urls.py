from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app import views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router = routers.DefaultRouter()
router.register(r'companies', views.CompanyViewSet)
router.register(r'estate', views.EstateViewSet)
router.register(r'estates', views.EstateGeoHyperlinkedViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Real Estate API",
        default_version='v1',
        description="Esta api es para aprender Django, CRUD Inmobiliaria",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="lumarjose@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger',
                                         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
                                       cache_timeout=0), name='schema-redoc'),
    path('api/v1/', include('app.urls')),
    path('api/v2/', include(router.urls)),
]
