import requests
import json
from CRUD_pet.Main_Endpoint import MainEndpoint
import logging
import allure

class CreatePet(MainEndpoint):

    def new_pet(self, data):
        with allure.step('Create Pet'):
            self.responce = requests.post('https://petstore.swagger.io/v2/pet', json=data)
            self.responce_json = self.responce.json()
            logging.getLogger().info(data)   #json.dumps(self.responce_json, indent=4)

    def check_id_pet(self, pet_id):
        with allure.step('Check Pet ID'):
            assert str(self.responce_json['id']) == pet_id
            logging.getLogger().info(pet_id)  #self.responce_json['id'], pet_id

