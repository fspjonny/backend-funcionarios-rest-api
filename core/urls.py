from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("v1/cadastro/admin/", admin.site.urls),
    path("", include('cadastro.urls')),
]

handler404 = "cadastro.views.views.handler404"
