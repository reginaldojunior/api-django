from rest_framework import routers, serializers, viewsets
from core.models import Employee, Andress
from serializers import AndressSerializer, EmployeeSerialize

class AndressViewSet(viewsets.ModelViewSet):
    queryset = Andress.objects.all()
    serializer_class = AndressSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerialize