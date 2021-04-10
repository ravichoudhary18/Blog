from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from blog.views import HomeView, SettingView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", HomeView.as_view(), name="home"),
    path("setting/", SettingView.as_view(),name='setting'),
    path('', include('blog.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('auth/', include('authentication.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
