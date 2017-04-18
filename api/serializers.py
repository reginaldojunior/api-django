from rest_framework import routers, serializers, viewsets
from core.models import Employee


class EmployeeSerialize(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Employee
        fields = ('__all__')
