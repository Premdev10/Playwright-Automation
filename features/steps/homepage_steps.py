from behave import given, when, then ,step
from utils.excel_reader import ExcelReader
from Pages.home_page import HomePage

@then('user validates the dynamic id field is present on the dashboard')
def step_impl(context):
    home_page= HomePage(context.page)
    home_page.validate_dynamic_id_field()

@then('user validates the hidden element is visible and becomes invisible after clicks')
def validate_hid_element(context):
    home_page=HomePage(context.page)
    home_page.validate_hidden_element()

@then('user validates the delayed content loaded successfully')
def validate_delayed_content(context):
    home_page=HomePage(context.page)
    home_page.validate_delayed_content_loaded()

@then('user validates the alert shown successfully')
def validate_alert(context):
    home_page=HomePage(context.page)
    home_page.validate_alertpresent()


