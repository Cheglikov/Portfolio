from pages.main_page_lan import MainPageLan


def test_button_lan_selector_exist(browser):
    main_page = MainPageLan(browser)
    main_page.open()
    assert MainPageLan.button_is_displayed

def test_button_lan_selector_clicked(browser):
    main_page = MainPageLan(browser)
    main_page.open()
    main_page.button_click()
    main_page.button_ua()
    assert MainPageLan.button_ua_is_displayed



