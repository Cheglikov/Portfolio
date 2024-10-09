from Data import *
import requests
import json
import pytest
import logging


@pytest.fixture()
def create_pet_id(data=data):
    responce = requests.post('https://petstore.swagger.io/v2/pet', json=data).json()
    yield responce['id']
    requests.delete(f"https://petstore.swagger.io/v2/pet/{responce['id']}")


def test_new_pet(data=data):
    responce = requests.post('https://petstore.swagger.io/v2/pet', json=data).json()
    logging.getLogger().info(data)
    assert str(responce['id']) == data['id']

def test_find_pet_by_id(create_pet_id):
    responce = requests.get(f"https://petstore.swagger.io/v2/pet/{create_pet_id}", json=data).json()
    logging.getLogger().info(data)
    assert str(responce['id']) == data['id']

def test_update_pet(create_pet_id, data_new = data_new):
    responce = requests.put('https://petstore.swagger.io/v2/pet', json=data_new).json()
    logging.getLogger().info(data_new)
    assert responce['name'] == data_new['name']
    assert responce['status'] == data_new['status']

def test_delete_pet(create_pet_id):
    logging.getLogger().info(create_pet_id)
    responce = requests.delete(f"https://petstore.swagger.io/v2/pet/{create_pet_id}")
    assert responce.status_code == 200
    responce = requests.get(f"https://petstore.swagger.io/v2/pet/{create_pet_id}")
    assert responce.status_code == 404

pytest.main(['-v'])


