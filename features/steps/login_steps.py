from behave import given, when, then ,step
from utils.excel_reader import ExcelReader
from Pages.login_page import LoginPage


@given('the user navigates to the login page')
def goto_loginpage(context):
    login_page = LoginPage(context.page)
    login_page.goto_loginpage()

@when('the user enters credentials from sheet "{sheet_name}" with ID "{tc_id}"')
def step_impl(context, sheet_name, tc_id):
    # Fetch data dictionary from Excel row
    data = ExcelReader.get_row_data(sheet_name, tc_id)
    
    # Initialize the page object and enter credentials
    login_page = LoginPage(context.page)
    login_page.enter_credentials(data['username'], data['password'])

@when('clicks the login button')
def step_impl(context):
    login_page = LoginPage(context.page)
    login_page.click_login()
    login_page.enter_otp("123456")  # Enter the OTP after clicking login

@then('the user should be redirected to the dashboard')
def step_impl(context):
    login_page = LoginPage(context.page)
    login_page.verify_dashboard_redirect()

