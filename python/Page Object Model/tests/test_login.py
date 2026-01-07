from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

def test_login_positif(driver):
    login = LoginPage(driver)
    dashboard = DashboardPage(driver)

    login.open(URL)
    login.login("Admin", "admin123", enter=True)

    assert dashboard.is_dashboard_displayed()
    assert "Jason Miller" in dashboard.get_username()


def test_login_negatif_invalid_password(driver):
    login = LoginPage(driver)

    login.open(URL)
    login.login("Admin", "admin")

    assert login.get_error_message() == "Invalid credentials"


def test_login_negatif_username_is_null(driver):
    login = LoginPage(driver)

    login.open(URL)
    login.login(password="admin")

    assert login.get_required_message() == "Required"


def test_login_negatif_password_is_null(driver):
    login = LoginPage(driver)

    login.open(URL)
    login.login(username="Admin")

    assert login.get_required_message() == "Required"
