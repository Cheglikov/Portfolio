import requests
import json
from CRUD_pet.Main_Endpoint import MainEndpoint
import logging
import allure


class UpdatePet(MainEndpoint):

    def update_pet(self, data_new):
        with allure.step('Update Pet'):
            self.responce = requests.put('https://petstore.swagger.io/v2/pet', json=data_new)
            self.responce_json = self.responce.json()
            logging.getLogger().info(data_new)

    def check_name_pet(self, pet_name):
        with allure.step('Check Pet new Name'):
            assert str(self.responce_json['name']) == pet_name
            logging.getLogger().info(pet_name)

    def check_status_pet(self, pet_status):
        with allure.step('Check Pet new Status'):
            assert str(self.responce_json['status']) == pet_status
            logging.getLogger().info(pet_status)



