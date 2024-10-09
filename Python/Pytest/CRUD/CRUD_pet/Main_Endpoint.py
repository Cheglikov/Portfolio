import logging
import allure

class MainEndpoint:
    responce = None
    responce_json = None

    def check_responce_is_200(self):
        with allure.step('Check responce 200'):
            logging.getLogger().info(self.responce.status_code)
            assert self.responce.status_code == 200


