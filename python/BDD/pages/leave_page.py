from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class PIMPage(BasePage):

    # ===== LOCATORS =====
    HEADER = (By.XPATH, '//h6[@class="oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module"]')
    
    def is_leave_page_displayed(self):
        return self.wait_visible(self.HEADER).is_displayed()