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