from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

#Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Blog Post Api",
        default_version='v1',
        description="An Api for blog posts: Zuri internship by Joseph Ayemlo",
        terms_of_service="https://zuri-intern-portfolio-design.herokuapp.com/",
        contact=openapi.Contact(email="ayemlojoseph@gmail.com"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


#urls
urlpatterns = [
    path ('api/', include('blogPost.urls')),
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger',
                                 cache_timeout=0), name='schema-swagger-ui'),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)