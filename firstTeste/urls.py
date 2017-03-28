from django.conf.urls import include, url
from django.contrib import admin
from core.views import home
from rest_framework import routers, serializers, viewsets
from core.models import Employee, Andress
from views import EmployeeViewSet, AndressViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

router.register(r'employee', EmployeeViewSet)
router.register(r'andress', AndressViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^$', home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
]
