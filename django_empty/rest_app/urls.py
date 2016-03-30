from rest_framework import routers
from django.conf.urls import url, include

from . import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
        url(r'api/', include(router.urls), name='rest_api'),
        url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    ]
