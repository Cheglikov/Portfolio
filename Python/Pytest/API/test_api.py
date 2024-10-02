from Data import data, data_new
import requests
import json
import pytest

@pytest.fixture()
def create_pet_id(data=data):
    responce = requests.post('https://petstore.swagger.io/v2/pet', json=data).json()
    yield responce['id']
    requests.delete(f"https://petstore.swagger.io/v2/pet/{responce['id']}")


def test_new_pet(data=data):
    responce = requests.post('https://petstore.swagger.io/v2/pet', json=data).json()
    print(json.dumps(responce, indent=4))
    assert str(responce['id']) == data['id']

def test_find_pet_by_id(create_pet_id):
    responce = requests.get(f"https://petstore.swagger.io/v2/pet/{create_pet_id}", json=data).json()
    print(json.dumps(responce, indent=4))
    assert str(responce['id']) == data['id']

def test_update_pet(create_pet_id, data_new = data_new):
    responce = requests.put('https://petstore.swagger.io/v2/pet', json=data_new).json()
    print(json.dumps(responce, indent=4))
    assert responce['name'] == data_new['name']
    assert responce['status'] == data_new['status']

def test_delete_pet(create_pet_id):
    print(create_pet_id)
    responce = requests.delete(f"https://petstore.swagger.io/v2/pet/{create_pet_id}")
    assert responce.status_code == 200
    responce = requests.get(f"https://petstore.swagger.io/v2/pet/{create_pet_id}")
    assert responce.status_code == 404



