from behave import given, when, then
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from config.config import LOGIN_URL

@given("user membuka halaman login")
def step_open_login(context):
    context.login = LoginPage(context.driver)
    context.login.open(LOGIN_URL)

@when('user login dengan username "{username}" dan password "{password}"')
def step_login_full(context, username, password):
    context.login.login(username=username, password=password, enter=True)

@when('user login dengan password "{password}"')
def step_login_no_username(context, password):
    context.login.login(password=password)

@when('user login dengan username "{username}"')
def step_login_no_password(context, username):
    context.login.login(username=username)

@then('user berhasil masuk ke "{message}"')
def step_verify_dashboard(context, message):
    dashboard = DashboardPage(context.driver)
    assert dashboard.is_dashboard_displayed()
    assert dashboard.get_dashboard_title() == message

@then('muncul pesan error "{message}"')
def step_verify_error(context, message):
    assert context.login.get_error_message() == message

@then('muncul pesan error field "{message}"')
def step_verify_required(context, message):
    assert context.login.get_required_message() == message
