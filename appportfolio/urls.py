from django.urls import path, re_path
from django.views.static import serve
from .views import *
from django.conf import settings

urlpatterns = [
    path('', homeView, name='home'),
    re_path(r'^sitemap\.xml$', serve, {'path': 'sitemap.xml', 'document_root': settings.BASE_DIR}),
]