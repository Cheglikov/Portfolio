from pages.main_page_lan import MainPageLan
import pytest


def test_button_lan_selector_exist(chrome_browser):
    main_page = MainPageLan(chrome_browser)
    main_page.open()
    assert MainPageLan.button_is_displayed

def test_button_lan_selector_clicked(chrome_browser):
    main_page = MainPageLan(chrome_browser)
    main_page.open()
    main_page.button_click()
    main_page.button_ua()
    assert MainPageLan.button_ua_is_displayed



pytest.main(['-v'])
