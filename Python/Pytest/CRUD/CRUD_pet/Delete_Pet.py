import requests
from CRUD_pet.Main_Endpoint import MainEndpoint
import json
import logging
import allure


class DeletePet(MainEndpoint):

    def delete_pet(self, pet_id):
        with allure.step('Delete Pet'):
            self.responce = requests.delete(f"https://petstore.swagger.io/v2/pet/{pet_id}")
            self.responce_json = self.responce.json()

    def check_responce_is_404(self):
        with allure.step('Check responce 404'):
            logging.getLogger().info(self.responce.status_code)
            assert self.responce.status_code == 404

    def find_by_id_after_delete(self, data):
        with allure.step('Find Pet after delete'):
            self.responce = requests.get(f"https://petstore.swagger.io/v2/pet/{data['id']}", json=data)
            self.responce_json = self.responce.json()
            logging.getLogger().info(data)