import os
import json
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "person_service.settings")

import django
django.setup()

from django.test.client import RequestFactory
from api.views import person_service_api


def test_get_all():
    factory = RequestFactory()
    request = factory.get('/api/v1/persons')
    response = person_service_api(request)
    assert response.status_code == 200

def test_get_id_existing():
    factory = RequestFactory()
    data = {
        "name": "test",
        "age": 0,
        "address": "test",
        "work": "test"
    }
    request = factory.post('/api/v1/persons/', data, content_type='application/json')
    response = person_service_api(request)

    location = response.headers["Location"]
    id = int(location[location.rfind("/") + 1:])

    request = factory.get('/api/v1/persons/')
    response = person_service_api(request, id)

    assert response.status_code == 200

    request = factory.delete('/api/v1/persons/')
    person_service_api(request, id)

# def test_get_id_non_existing():
#     factory = RequestFactory()
#     request = factory.get('/api/v1/persons/')
#     response = person_service_api(request, 0)
#     assert response.status_code == 404

def test_put():
    factory = RequestFactory()
    data = {
        "name": "test",
        "age": 0,
        "address": "test",
        "work": "test"
    }
    request = factory.post('/api/v1/persons/', data, content_type='application/json')
    response = person_service_api(request)

    assert response.status_code == 201

    location = response.headers["Location"]
    id = int(location[location.rfind("/") + 1:])
    request = factory.delete('/api/v1/persons/')
    person_service_api(request, id)

def test_put_bad():
    factory = RequestFactory()
    data = {
        "nice": "ok",
    }
    request = factory.post('/api/v1/persons/', data, content_type='application/json')
    response = person_service_api(request)

    assert response.status_code == 400

def test_delete_existing():
    factory = RequestFactory()
    request = factory.delete('/api/v1/persons/')
    response = person_service_api(request, 1)
    assert response.status_code == 204

def test_delete_non_existing():
    factory = RequestFactory()
    request = factory.delete('/api/v1/persons/')
    response = person_service_api(request, -1)
    assert response.status_code == 204