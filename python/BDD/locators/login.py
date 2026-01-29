from selenium.webdriver.common.by import By

# ===== LOCATORS =====
class LoginLoc:
    USERNAME = (By.XPATH, '//input[@name="username"]')
    PASSWORD = (By.XPATH,  '//input[@name="password"]')
    LOGIN_BTN = (By.XPATH, '//button[@type="submit"]')
    ERROR_CREDENTIAL = (By.XPATH, '//p[@class="oxd-text oxd-text--p oxd-alert-content-text"]')
    ERROR_REQUIRED = (By.XPATH, '//span[@class="oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message"]')
