# Завдання: за допомогою браузера (Selenium) відкрити форму за наступним посиланням:
# https://docs.google.com/forms/d/e/1FAIpQLScLhHgD5pMnwxl8JyRfXXsJekF8_pDG36XtSEwaGsFdU2egyw/viewform?usp=sf_link
# заповнити і відправити її.
# Зберегти два скріншоти: заповненої форми і повідомлення про відправлення форми.
# В репозиторії скріншоти зберегти.
# Корисні посилання:
# https://www.selenium.dev/documentation/
# https://chromedriver.chromium.org/downloads

from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = wd.ChromeOptions()
options.add_argument("--no-sandbox")
url_adress = 'https://docs.google.com/forms/d/e/1FAIpQLScLhHgD5pMnwxl8JyRfXXsJekF8_pDG36XtSEwaGsFdU2egyw/viewform?usp=sf_link'
name = 'Andrii_Bezkrovnyi'

driver = wd.Chrome(executable_path='./chromedriver', options=options)
driver.get(url_adress)
wait = WebDriverWait(driver, 10)

block = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[role="listitem"]')))
input_field = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="text"]')))

input_field.send_keys(name)
driver.save_screenshot('first_screen.png')
submit_button = driver.find_element(By.CSS_SELECTOR, 'div[jsname="M2UYVd"]')
submit_button.click()
new_page = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.freebirdFormviewerViewResponseConfirmContentContainer')))
driver.save_screenshot('second_screen.png')


driver.close()



