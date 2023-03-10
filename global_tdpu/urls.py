from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='Django API',
        default_version='v1',
        description='Test description',
        license=openapi.License(name='BSD License'),
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/api/', include("accounts.urls")),
    path('blog/api/', include('blog.urls')),
    path('comment/', include('comment.urls')),
    path('news/api/', include('news.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


