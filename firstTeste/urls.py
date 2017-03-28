from django.conf.urls import include, url
from django.contrib import admin
from core.views import home
from rest_framework import routers, serializers, viewsets
from core.models import Employee, Andress
from views import EmployeeViewSet, AndressViewSet
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='API Employee')

router = routers.DefaultRouter()

router.register(r'employee', EmployeeViewSet)
router.register(r'andress', AndressViewSet)

urlpatterns = [
    url(r'^docs/', schema_view),
    url(r'^api/', include(router.urls)),
    url(r'^$', home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
]
