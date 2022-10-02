from django.contrib import admin
from django.urls import path
from main.views import index, blog, posting
from.views import *

from django.conf.urls.static import static
from django.conf import settings

app_name = 'main'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('blog/', blog, name='blog'),
    path('blog/<int:pk>/', posting, name='posting'),
    path('fileupload/', fileUpload, name="fileupload"),
    path('blog/new_post/', new_post, name="new_post"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



