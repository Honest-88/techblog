from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('posts.urls')),
    path('',include('extras.urls')),
    path('users/',include('users.urls')),
    path('tinymce/', include('tinymce.urls')),


] 
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

#+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
