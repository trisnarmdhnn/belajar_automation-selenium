from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.login import LoginLoc

class LoginPage(BasePage):

    def open(self, url):
        self.driver.get(url)

    def login(self, username="", password="", enter=False):
        if username:
            self.input_text(LoginLoc.USERNAME, username)
        if password:
            self.input_text(LoginLoc.PASSWORD, password)
        if enter:
            self.wait_visible(LoginLoc.PASSWORD).send_keys(Keys.ENTER)
        else:
            self.click(LoginLoc.LOGIN_BTN)

    def get_error_message(self):
        #return self.get_text(self.ERROR_CREDENTIAL)
        return self.wait_visible(LoginLoc.ERROR_CREDENTIAL).text

    def get_required_message(self):
        #return self.get_text(self.ERROR_REQUIRED)
        return self.wait_visible(LoginLoc.ERROR_REQUIRED).text
