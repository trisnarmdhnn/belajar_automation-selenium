from behave import given, when, then
from pages.admin_page import AdminPage

@given('user berada di halaman "{page}"')
def step_user_on_dashboard_page(context,page):
    assert context.dashboard.is_dashboard_displayed()
    assert context.dashboard.get_dashboard_title() == page


@when('user klik navigasi admin')
def step_click_nav_admin(context):
    context.admin = AdminPage(context.driver)
    context.admin.open_admin_page()

@then('user berhasil membuka halaman "Admin"')
def step_verify_admin(context):
    assert context.admin.is_admin_page_displayed()


@when(u'user klik navigasi pim')
def step_impl(context):
    raise StepNotImplementedError(u'When user klik navigasi pim')


@then(u'user berhasil membuka halaman "PIM"')
def step_impl(context):
    raise StepNotImplementedError(u'Then user berhasil membuka halaman "PIM"')


@when(u'user klik navigasi leave')
def step_impl(context):
    raise StepNotImplementedError(u'When user klik navigasi leave')


@then(u'user berhasil membuka halaman "Leave"')
def step_impl(context):
    raise StepNotImplementedError(u'Then user berhasil membuka halaman "Leave"')