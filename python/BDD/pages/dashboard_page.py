from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.dashboard import DashboardLoc
from locators.navbar import NavbarLoc

class DashboardPage(BasePage):

    def is_dashboard_displayed(self):
        return self.wait_visible(DashboardLoc.DASHBOARD_HEADER).is_displayed()
        
    def get_dashboard_title(self):
        return self.get_text(DashboardLoc.DASHBOARD_HEADER)

    def get_username(self):
        return self.get_text(DashboardLoc.USERNAME)
    
    def is_pim_page_displayed(self):
        return self.wait_visible(DashboardLoc.DASHBOARD_HEADER).is_displayed()
        self.click(NavbarLoc.PIM)

    def is_leave_page_displayed(self):
        return self.wait_visible(DashboardLoc.DASHBOARD_HEADER).is_displayed()
        self.click(NavbarLoc.LEAVE)
    
    def is_admin_page_displayed(self):
        return self.wait_visible(DashboardLoc.DASHBOARD_HEADER).is_displayed()
        self.click(NavbarLoc.ADMIN)