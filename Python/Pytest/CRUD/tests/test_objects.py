from CRUD_pet.Data import *
from CRUD_pet.Create_pet import CreatePet
from CRUD_pet.Find_pet_by_id import FindPetById
from CRUD_pet.Update_pet import UpdatePet
from CRUD_pet.Delete_Pet import DeletePet
import pytest
import allure

@allure.feature('test_object')
@allure.story('Create pet')
@allure.title('Create pet')
def test_new_pet(create_pet_id):
    create_pet = CreatePet()
    create_pet.new_pet(data=data)
    create_pet.check_id_pet(pet_id=data['id'])
    create_pet.check_responce_is_200()

@allure.feature('test_object')
@allure.story('Find pet')
@allure.title('Find pet by ID')
def test_find_pet_by_id(create_pet_id, data = data):
    find_pet = FindPetById()
    find_pet.find_by_id(data)
    find_pet.check_pet_id(pet_id=data['id'])
    find_pet.check_pet_name(pet_name=data['name'])
    find_pet.check_responce_is_200()

@allure.feature('test_object')
@allure.story('Update pet')
@allure.title('Update pet')
def test_update_pet(create_pet_id, data_new = data_new):
    update_pet = UpdatePet()
    update_pet.update_pet(data_new=data_new)
    update_pet.check_name_pet(pet_name=data_new['name'])
    update_pet.check_status_pet(pet_status=data_new['status'])
    update_pet.check_responce_is_200()

@allure.feature('test_object')
@allure.story('Delete pet')
@allure.title('Delete pet')
def test_delete_pet(create_pet_id, data = data):
    delete_pet = DeletePet()
    delete_pet.delete_pet(data['id'])
    delete_pet.check_responce_is_200()
    delete_pet.find_by_id_after_delete(data)
    delete_pet.check_responce_is_404()


#pytest.main(['-v'])

