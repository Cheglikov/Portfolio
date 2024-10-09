from CRUD_pet.Data import *
from CRUD_pet.Create_pet import CreatePet
from CRUD_pet.Delete_Pet import DeletePet
import pytest
import allure



@allure.title('Create and Delete Pet')
@pytest.fixture()
def create_pet_id(data=data):
    create_pet = CreatePet()
    create_pet.new_pet(data=data)
    yield create_pet.responce_json['id']
    delete_pet = DeletePet()
    delete_pet.delete_pet(data)


