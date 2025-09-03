from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from ustudy import settings

schema_view = get_schema_view(
    openapi.Info(
        title="UStudy API",
        default_version="v1",
        description="API documentation for UStudy project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@ustudy.uz"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include([
        path('Attendance/', include('Attendance.urls')),
        path('Payment/', include('Payment.urls')),
        path('Group/', include('Group.urls')),
        path('User/', include('User.urls')),
        path('Student/', include('Student.urls')),
        path('StudentGroup/', include('StudentGroup.urls')),
        path('Course/', include('Course.urls')),

    ])),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger',
                                         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
                                       cache_timeout=0), name='schema-redoc'),

]

if settings.DEBUG:  # faqat developmentda ishlaydi
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
