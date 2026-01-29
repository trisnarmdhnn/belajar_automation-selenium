from selenium.webdriver.common.by import By

# ===== LOCATORS =====
class DashboardLoc:
    HEADER = (By.XPATH, '//h6[@class="oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module"]')
    USERNAME = (By.XPATH, '//p[@class="oxd-userdropdown-name"]')