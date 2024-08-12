import datetime
import time
from datetime import datetime
import os

from selenium import webdriver
from selenium.common import ElementNotInteractableException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


driver = webdriver.Chrome()
url = 'https://zdorovi.ua/'

wait = WebDriverWait(driver, 10)

date = datetime.now().strftime("%Y-%m-%d_%H_%M_%S")

file_name = os.path.basename("Selenium_Python.py")
file = file_name[:-3]
file = file.title()
print(file)
name_screenshot = file + '_Screenshot_' + date + '.png'
name_file = file + '_Test_result_' + date + '.txt'

file_test = open(r'C:\Users\Admin\PycharmProjects\pythonProject4\Test_result\\' + name_file, 'w', -1, 'utf-8')

driver.get(url)
driver.maximize_window()
driver.refresh()

wait.until(EC.title_contains('Пошук'))

curently_city = driver.find_element(By.XPATH, '//*[contains(@style,"location")]')
curently_city.click()

#wait.until(EC.text_to_be_present_in_element_value((By.XPATH, '//*[@placeholder="Вкажіть назву населеного пункту"]'), "Вкажіть назву населеного пункту"))

time.sleep(10)

change_city = driver.find_element(By.XPATH, '//*[@placeholder="Вкажіть назву населеного пункту"]')
change_city.click()

time.sleep(10)

input_city = driver.find_element(By.XPATH, '//*[@placeholder="Вкажіть назву населеного пункту"]')
input_city.clear()
time.sleep(5)
input_city.send_keys("Чугуїв")

time.sleep(5)

Chuhuiv_city = driver.find_element(By.XPATH, '//*[text()=" Чугуїв (Харківська обл.) "]')
Chuhuiv_city.click()

time.sleep(5)

driver.find_element(By.XPATH, '//*[@class="header-close-btn"]').click()

driver.refresh()
time.sleep(10)

faq_desktop = driver.find_element(By.XPATH, "//div[@class='faq-desktop']")
faq_desktop.click()
time.sleep(10)

faq_desktop_back = driver.find_element(By.XPATH, "//span[text()='ffff']").click()
time.sleep(10)

input_name = driver.find_element(By.ID, "livePrSearch")
input_name.clear()
time.sleep(10)

input_name.send_keys("Корвалолл")
time.sleep(3)
input_name.send_keys(Keys.BACKSPACE)
time.sleep(3)
input_name.send_keys(Keys.BACKSPACE)
time.sleep(5)

input_name.clear()
input_name.send_keys("Корвалол")
time.sleep(10)

#driver.execute_script("window.scrollTo(0, -200)")
#time.sleep(10)

input_korvalol = driver.find_element(By.XPATH, '//*[@class="content-number"][text()="4 товари"]')
input_korvalol.click()
time.sleep(10)

korvalol_2 = driver.find_element(By.XPATH, '//*[@class="bz-product-title"][text()="Корвалол табл. №30 (10х3)"]')
korvalol_2.click()
time.sleep(5)

driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.XPATH, '//*[@class="all-btn-text"][text()="поділитися"]'))
#driver.execute_script("window.scrollTo(0, 800)")
time.sleep(3)

driver.find_element(By.XPATH, '//*[@class="inner-span"][text()="Вибрати аптеку"]').click()
time.sleep(10)

driver.find_element(By.XPATH, '//*[text()="Аптека низькі ціни №1"]/following-sibling::div/descendant::span').click()
time.sleep(10)

driver.find_element(By.XPATH, '//*[text()="Перейти до кошика"]').click()
time.sleep(10)

driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.XPATH, '//*[text()="Упаковка"]'))
time.sleep(3)

driver.find_element(By.XPATH, '//div[@class="bz-product-details"]/descendant::button[@aria-label="minus"][1]').click()
time.sleep(5)

driver.find_element(By.XPATH, '//div[@class="bz-product-details"]/descendant::button[@aria-label="plus"][2]').click()
time.sleep(5)

driver.find_element(By.XPATH, '//*[text()="Замовити"]').click()
time.sleep(5)

driver.save_screenshot(r'C:\Users\Admin\PycharmProjects\pythonProject4\Screen\\' + name_screenshot)

total = driver.find_element(By.XPATH, '//*[contains(text(),"Сума")][@class="items-sum"]').text
print(f'Вартість одного блістеру - {float(total[6:-5])/2}')


file_test.write(f'Вартість одного блістеру - {float(total[6:-5])/2}' + '\n' + "Test over" + '\n')
file_test.close()

time.sleep(5)


