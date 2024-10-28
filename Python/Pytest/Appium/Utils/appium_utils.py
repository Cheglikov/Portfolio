from appium import webdriver
from appium.options.android import UiAutomator2Options
import pytest


capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.google.android.apps.nexuslauncher',
    appActivity='.NexusLauncherActivity',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'
capabilities_options = UiAutomator2Options().load_capabilities(capabilities)

@pytest.fixture()
def driver():
    app_driver = webdriver.Remote(appium_server_url, options=capabilities_options)
    yield app_driver
    if app_driver:
        app_driver.quit()

