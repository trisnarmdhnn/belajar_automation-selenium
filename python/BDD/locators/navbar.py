from selenium.webdriver.common.by import By

# ===== LOCATORS =====
class NavbarLoc:
    NAV_ADMIN = (By.XPATH, '//a[.//span[normalize-space()="Admin"]]')
    NAV_PIM = (By.XPATH, '//span[@text()="PIM"]')
    NAV_LEAVE = (By.XPATH, '//span[@text()="Leave"]')
    NAV_TIME = (By.XPATH, '//span[@text()="Time"]')
    NAV_RECRUITMENT = (By.XPATH, '//span[@text()="Recruitment"]')
    NAV_MYINFO = (By.XPATH, '//span[@text()="My Info"]')
    NAV_PERFORMANCE = (By.XPATH, '//span[@text()="Performance"]')
    NAV_DASHBOARD = (By.XPATH, '//span[@text()="Dashboard"]')
    NAV_DIRECTORY = (By.XPATH, '//span[@text()="Directory"]')
    NAV_MAINTENANCE = (By.XPATH, '//span[@text()="Maintenance"]')
    NAV_CLAIM = (By.XPATH, '//span[@text()="Claim"]')
    NAV_BUZZ = (By.XPATH, '//span[@text()="Buzz"]')