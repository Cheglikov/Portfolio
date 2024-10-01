from selenium import webdriver
import pytest
import time

@pytest.fixture()
def browser():
    chrome_browser = webdriver.Chrome()
    chrome_browser.maximize_window()
    chrome_browser.refresh()
    chrome_browser.implicitly_wait(10)
    return chrome_browser


