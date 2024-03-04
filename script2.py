from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.get("https://www.linkedin.com/home")
driver.maximize_window()
time.sleep(3)

uName = driver.find_element('name', "session_key")
uName.send_keys("indrani.b2022@gmail.com")
uPassword = driver.find_element('name', "session_password")
uPassword.send_keys("Indrani_B@2022")
# driver.find_element(By.CSS_SELECTOR, "button.sign-in-form__submit-btn--full-width").click()
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search']").send_keys("Indrani Bhattacharjee")
time.sleep(10)

driver.find_element(By.CSS_SELECTOR, "span[class='search-global-typeahead-hit__text t-16 t-black']").click()
time.sleep(60)

