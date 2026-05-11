from locators.navbar import NavbarLoc
from pages.base_page import BasePage
from locators.admin import AdminLoc

class AdminPage(BasePage):
    
    def open_admin_page(self):
        self.click(NavbarLoc.NAV_ADMIN)
    
    def is_admin_page_displayed(self):
        return self.wait_visible(AdminLoc.HEADER_ADMIN).is_displayed()