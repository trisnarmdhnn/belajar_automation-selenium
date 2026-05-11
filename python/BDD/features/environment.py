from selenium import webdriver # berfungsi untuk menjalankan webdriver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from config.config import LOGIN_URL

print("=== ENVIRONMENT.PY TERLOAD ===")

def before_scenario(context, scenario): # menyatakan bahwa code ini akan dijalankan sebelum menjalankan skenario
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True) # berfungsi agar browser tidak tertutup setelah testcase selesai

    context.driver = webdriver.Chrome(options) # Open browser
    context.driver.maximize_window() # membesarkan jendela browser
    
    if "login" in scenario.effective_tags: # tag ini berfungsi sebagai hook, sehingga setiap skenario yang memiliki tag @login akan menjalankan perinta ini
        context.login = LoginPage(context.driver) # memanggil class LoginPage pada file login_page kemudian menyimpan nya pada variable login
        context.login.open(LOGIN_URL) # memanggil function 'open' pada file login_step untuk membuka 'Login_URL'
        context.login.login("Admin", "admin123")# memanggil function 'login' pada file login_step dan memberikan value untuk input username dan password

        context.dashboard = DashboardPage(context.driver) # memanggil class DashboardPage pada file dashboard_page kemudian menyimpan nya pada variable dashboard
        assert context.dashboard.is_dashboard_displayed() # melakukan validasi dengan memanggil function 'is_dashboard_displayed()'
        assert context.dashboard.get_dashboard_title() # melakukan validasi dengan memanggil function 'get_dashboard_title()'

def after_scenario(context, scenario): # menyatakan bahwa code ini akan dijalankan setelah menjalankan skenario
    context.driver.quit() # tutup browser

# ===== PENJELASAN =====
# file ini berfungsi untuk melakukan setup (sebelum eksekusi) dan teardown (setelah eksekusi) testcase