from behave import given, when, then, step
from utils.excel_reader import ExcelReader
from Pages.HR_page import HRpage


@then('user clicks on HR tab')
def step_impl(context):
    hr_page = HRpage(context.page)
    hr_page.click_on_hrpage()

@then('verify user eneters in to the HR section')
def user_enters_hr_section(context):
    hr_page = HRpage(context.page)
    hr_page.verify_hr_dashboard()

@then('verify the total entries in the table')
def verify_total_entries_inthe_table(context):
    hr_page = HRpage(context.page)
    hr_page.verify_employee_table()


