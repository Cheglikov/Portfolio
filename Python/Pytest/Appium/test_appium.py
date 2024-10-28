import pytest
from appium.webdriver.common.appiumby import AppiumBy
import time
from Utils.appium_utils import driver


@pytest.mark.app
def test_find_battery(driver) -> None:
    el_settings = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Settings"]')
    el_settings.click()
    time.sleep(3)
    location_settings = driver.find_element(
        by=AppiumBy.ANDROID_UIAUTOMATOR,
        value='new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(text("Settings"))'
    )
    location_settings.click()
    batterry = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
    batterry.click()
    time.sleep(3)

    batterry_back = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageButton[@content-desc='
                                                                 '"Navigate up"]')
    batterry_back.click()
    time.sleep(3)
    location_settings = driver.find_element(
        by=AppiumBy.ANDROID_UIAUTOMATOR,
        value='new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(text("Settings"))'
    )
    location_settings.click()
    driver.press_keycode(3)
    time.sleep(3)

@pytest.mark.app
def test_find_location(driver) -> None:
    el_settings = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Settings"]')
    el_settings.click()
    time.sleep(3)
    location = driver.find_element(
        by=AppiumBy.ANDROID_UIAUTOMATOR,
        value='new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(text("Location"))'
    )
    location.click()
    time.sleep(3)
    use_location = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Use location"]')
    use_location.click()
    time.sleep(3)
    use_location = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Use location"]')
    use_location.click()
    time.sleep(3)
    batterry_back = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageButton[@content-desc='
                                                                 '"Navigate up"]')
    batterry_back.click()
    time.sleep(3)
    driver.press_keycode(3)
    time.sleep(3)


