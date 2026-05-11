import json
import os
from behave import given, when, then #digunakan untuk import gherkin
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from config.config import LOGIN_URL

@given("user membuka halaman login") # digunakan untuk mendefinisikan step yang akan dijalankan
def step_open_login(context): # digunakan untuk menyimpan instance driver pada variable login
    context.login = LoginPage(context.driver) # memanggil class LoginPage pada file login_page kemudian menyimpannya pada variable login
    context.login.open(LOGIN_URL) # memanggil function 'open' pada file login_page untuk membuka 'Login_URL'

@when('user login menggunakan data "{data_key}"')
def step_login_with_json_data(context, data_key):
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) # digunakan untuk menentukan lokasi folder root
    json_path = os.path.join(base_dir, 'data', 'credentials.json') # digunakan untuk menentukan lokasi file json
    
    with open(json_path, 'r') as file: # digunakan untuk membaca file json dengan 'r' berarti 'Read'
        data = json.load(file) # digunakan untuk memuat file json ke dalam variable data 
        
    user_data = data[data_key] # digunakan untuk mengambil data dari file json berdasarkan key yang diberikan
    username = user_data.get("username", "") # digunakan untuk mengambil data username dari file json berdasarkan key yang diberikan
    password = user_data.get("password", "") # digunakan untuk mengambil data password dari file json berdasarkan key yang diberikan
    
    context.login.login(username=username, password=password) # digunakan untuk memasukkan username dan password ke dalam field login

@then('user berhasil masuk ke "{page}"')
def step_verify_dashboard(context, page):
    dashboard = DashboardPage(context.driver)
    assert dashboard.is_dashboard_displayed()
    assert dashboard.get_dashboard_title() == page

@then('muncul pesan error "{message}"')
def step_verify_error(context, message):
    assert context.login.get_error_message() == message

@then('muncul pesan error field "{message}"')
def step_verify_required(context, message):
    assert context.login.get_required_message() == message
