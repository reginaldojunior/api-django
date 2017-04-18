from rest_framework import routers, serializers, viewsets
from core.models import Employee
from serializers import EmployeeSerialize

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerialize