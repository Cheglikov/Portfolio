import requests
import json
from CRUD_pet.Main_Endpoint import MainEndpoint
import logging
import allure

class FindPetById(MainEndpoint):

    def find_by_id(self, data):
        with allure.step('Find Pet'):
            self.responce = requests.get(f"https://petstore.swagger.io/v2/pet/{data['id']}", json=data)
            self.responce_json = self.responce.json()
            logging.getLogger().info(data)

    def check_pet_name(self, pet_name):
        with allure.step('Check Pet Name'):
            assert self.responce_json['name'] == pet_name
            logging.getLogger().info(pet_name)

    def check_pet_id(self, pet_id):
        with allure.step('Check Pet ID'):
            assert str(self.responce_json['id']) == pet_id
            logging.getLogger().info(pet_id)



