"""
URLs for the Skills List API
API allows anyone access to list, create, update, and delete skills
"""
from django.contrib import admin
from django.urls import path, include, re_path
from api import views
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':
    settings.MEDIA_ROOT}), #serve media files when deployed
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root':
    settings.STATIC_ROOT}), #serve static files when deployed
    path('', views.skillsList.as_view()),
    path('api/skillsList/', views.skillsList.as_view()),
    path('api/skills/', views.skillsListCreate.as_view()),
    path('api/skills/<int:pk>', views.skillRetrieveUpdateDestroy.as_view()),
]
