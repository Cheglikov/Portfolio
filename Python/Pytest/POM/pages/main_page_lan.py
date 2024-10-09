import time
from pages.main_page import MainPage
from selenium.webdriver.common.by import By


button_lan_selector = (By.XPATH, "//*[text()='ru']")
button_lan_selector_UA = (By.XPATH, "//*[text()='ua']")
url = 'https://zdorovi.ua/'

class MainPageLan(MainPage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get(url)

    def button(self):
        return self.find(button_lan_selector)

    @property
    def button_is_displayed(self):
        return self.button().is_displated()

    def button_click(self):
        self.button().click()
        time.sleep(5)

    def button_text(self):
        self.button().text()

    def button_ua(self):
        return self.find(button_lan_selector_UA)

    @property
    def button_ua_is_displayed(self):
        return self.button_ua().is_displated()

    def button_ua_text(self):
        self.button_ua().text()