from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class LoginPage(BasePage):

    # ===== LOCATORS =====
    USERNAME = (By.XPATH, '//input[@name="username"]')
    PASSWORD = (By.XPATH,  '//input[@name="password"]')
    LOGIN_BTN = (By.XPATH, '//button[@type="submit"]')
    ERROR_CREDENTIAL = (By.XPATH, '//p[@class="oxd-text oxd-text--p oxd-alert-content-text"]')
    ERROR_REQUIRED = (By.XPATH, '//span[@class="oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message"]')

    def open(self, url):
        self.driver.get(url)

    def login(self, username="", password="", enter=False):
        if username:
            self.input_text(self.USERNAME, username)
        if password:
            self.input_text(self.PASSWORD, password)

        if enter:
            self.wait_visible(self.PASSWORD).send_keys(Keys.ENTER)
        else:
            self.click(self.LOGIN_BTN)

    def get_error_message(self):
        #return self.get_text(self.ERROR_CREDENTIAL)
        return self.wait_visible(self.ERROR_CREDENTIAL).text

    def get_required_message(self):
        #return self.get_text(self.ERROR_REQUIRED)
        return self.wait_visible(self.ERROR_REQUIRED).text
