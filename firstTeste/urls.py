from django.conf.urls import include, url
from django.contrib import admin
from core.views import home
from rest_framework import routers, serializers, viewsets
from core.models import Employee, Andress

class AndressSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Andress

        fields = ('id', 'street', 'number', 'neighborhood', 'city', 'state', 'complement')

class EmployeeSerialize(serializers.HyperlinkedModelSerializer):	
    class Meta:
        model = Employee
	
        fields = ('id','name','document','birthday','phone','salary','gender', 'andress')

class AndressViewSet(viewsets.ModelViewSet):
    queryset = Andress.objects.all()
    serializer_class = AndressSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerialize

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'employee', EmployeeViewSet)
router.register(r'andress', AndressViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'firstTeste.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api/', include(router.urls)),
    url(r'^$', home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
]
