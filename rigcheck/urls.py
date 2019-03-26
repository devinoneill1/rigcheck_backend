from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    path('rigcheckapp/', include('rigcheckapp.urls')),
]
