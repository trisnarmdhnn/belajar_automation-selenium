from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

#Open browser and website
driver = webdriver.Chrome(option)
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')


#wait - explicitly
waitElementVisible = WebDriverWait(driver, timeout=10)
username = waitElementVisible.until(EC.visibility_of_element_located((By.XPATH, '//input[@name="username"]')))

#username = driver.find_element(By.XPATH, '//input[@name="username"]')
username.send_keys('Admin')

password = driver.find_element(By.XPATH, '//input[@name="password"]')
password.send_keys('admin')

btnLogin = driver.find_element(By.XPATH, '//button[@type="submit"]').click()

driver.implicitly_wait(10)

errorCred = driver.find_element(By.XPATH, '//p[@class="oxd-text oxd-text--p oxd-alert-content-text"]')

assert errorCred.text == "Invalid credentials"


