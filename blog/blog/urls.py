
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog_api.urls')),
    path('api-auth/', include('rest_framework.urls'))
]
