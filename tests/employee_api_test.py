import requests
import pytest
import json
from api.viewsets import EmployeeViewSet

import logging

logging.basicConfig(filename='example.log', level=logging.DEBUG)


@pytest.fixture
def temporary_employee():
    from core.models import Employee

    employee = Employee(
        name="Reginaldo",
        email="76regi@gmail.com",
        department="TI")
    employee.save()

    return employee


@pytest.mark.django_db
def test_montadora_viewset(temporary_employee):
    viewset = EmployeeViewSet()
    found = False
    for record_dict in viewset.queryset.values():
        if record_dict['name'] == "Reginaldo":
            found = True

    assert found is True


@pytest.mark.django_db
def test_update(client, temporary_employee):
    from core.models import Employee

    response = client.post('/api/employee/{}/'.format(temporary_employee.id),
                           json.dumps({"name": "Reginaldo Editado"}),
                           HTTP_X_METHOD_OVERRIDE='PUT',
                           content_type='application/json')

    found_employee = Employee.objects.filter(name="Reginaldo")

    assert "Reginaldo" not in found_employee


@pytest.mark.django_db
def test_delete(client, temporary_employee):
    from core.models import Employee

    response = client.post('/api/employee/{}/'.format(temporary_employee.id),
                           json.dumps({"id": temporary_employee.id}),
                           HTTP_X_METHOD_OVERRIDE='DELETE',
                           content_type='application/json')

    found_employee = Employee.objects.filter(name="Reginaldo")

    assert "Reginaldo" not in found_employee


@pytest.mark.django_db
def test_get(client, temporary_employee):
    response = client.get('/api/employee/{}/'.format(temporary_employee.id))
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_not_found(client, temporary_employee):
    response = client.get('/api/employee/46545456/')
    assert response.status_code == 404
