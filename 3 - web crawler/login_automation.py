from time import sleep
from selenium.webdriver.common.by import By
from connect_manager import ConnectToSite

url = 'https://practicetestautomation.com/practice-test-login/'

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# driver.get(url)
with ConnectToSite(url) as driver:
    all_text = driver.find_element(By.XPATH,'//*[@id="login"]/ul/li[2]')
    splitted_text = all_text.text.split(' ')

    password = splitted_text[-1]
    username = splitted_text[-2].split('\n')[0]

    username_input = driver.find_element(By.NAME, 'username')
    username_input.send_keys(username)

    password_input = driver.find_element(By.NAME, 'password')
    password_input.send_keys(password)

    submit_btn = driver.find_element(By.CLASS_NAME,'btn')
    submit_btn.click()
    #driver.execute_script("arguments[0].click();", submit_btn)

    sleep(5)
