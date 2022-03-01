from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static


urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('',include('core.urls',namespace='core')),
    path('api/',include('core.api.urls', namespace='subscribe_api')),
    
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)


