from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

url = 'https://practicetestautomation.com/practice-test-login/'

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get(url)

username_input = driver.find_element(By.NAME, 'username')
username_input.send_keys('student')

password_input = driver.find_element(By.NAME, 'password')
password_input.send_keys('Password123')

submit_btn = driver.find_element(By.CLASS_NAME,'btn')
submit_btn.click()

sleep(5)
driver.quit()