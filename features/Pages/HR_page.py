from playwright.sync_api import Page, expect
import allure
import json

class HRpage:
    beneficiary_name="Rahul"

    def __init__(self, page: Page):
        self.page = page

        #locators
        self.hr_button=page.get_by_test_id("dashboard-card-hr")
        self.employee_table=page.get_by_test_id("employees-table")
        self.employee_table_row=page.locator("//table//tbody//tr")


    def click_on_hrpage(self):
          expect(self.hr_button).to_be_visible()
          self.hr_button.click()

    def verify_hr_dashboard(self):
         expect(self.employee_table).to_be_visible()

    def verify_employee_table(self):
         total_row=self.employee_table_row.count()
         employee_names=list()
         for i in range(1, total_row + 1):
              self.employee_table_cell=self.page.locator(f"//table//tbody//tr[{i}]//td[2]")
              cell_value=self.employee_table_cell.text_content()
              employee_names.append(cell_value)

         allure.attach(
           json.dumps(employee_names, indent=2),
           name="employee_names",
           attachment_type=allure.attachment_type.JSON
         )
        