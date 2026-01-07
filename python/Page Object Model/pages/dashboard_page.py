from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):

    HEADER = (By.XPATH, '//h6[@class="oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module"]')
    USERNAME = (By.XPATH, '//p[@class="oxd-userdropdown-name"]')

    def is_dashboard_displayed(self):
        return self.wait_visible(self.HEADER).is_displayed()

    def get_username(self):
        return self.get_text(self.USERNAME)
