from playwright.sync_api import Page, expect
import allure
from allure_commons.types import AttachmentType

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        
        


        # Locators
        self.dynamic_id=page.locator('//button[contains(@id,"flaky-")]')
        self.hidden_element=page.get_by_text("You can see me!",exact=True)
        self.hide_ele_button=page.get_by_role("button",name="Hide element")
        self.delayed_header=page.get_by_text("Delayed / async loading")
        self.delayed_button=page.get_by_role("button",name="Load content")
        self.delayed_content=page.get_by_test_id("delayed-load-result")
        self.alert_button=page.locator("//button[text()='Alert']")
        self.prompt_button=page.locator("//button[text()='Prompt']")


    def validate_dynamic_id_field(self):
            if self.dynamic_id.is_visible():
                print("Dynamic id field is present on the dashboard.")
                flakyid=self.dynamic_id.text_content()
                print("Dynamic id field value is:",flakyid)
                self.dynamic_id.click()
                if self.dynamic_id.text_content()!=flakyid:
                    print("dynamic id changed")
                else:
                    print("dynamic id not changed")

            else:
                print("Dynamic id field is not present on the dashboard.")

    def validate_hidden_element(self):
         expect(self.hidden_element).to_be_visible()
         allure.attach(
              self.page.screenshot(),
              name="hidden element is present",
                attachment_type=AttachmentType.PNG
         )
         self.hide_ele_button.click()
         expect(self.hidden_element).to_be_hidden()
         allure.attach(
                       self.page.screenshot(),
                       name="hidden element is not present",
                         attachment_type=AttachmentType.PNG
                  )

    def validate_delayed_content_loaded(self):
         expect(self.delayed_header).to_be_visible()
         self.delayed_button.click()
         allure.attach(self.page.screenshot(),name="content is loading",attachment_type=AttachmentType.PNG)
         expect(self.delayed_content).to_be_visible(timeout=50000)
         allure.attach(self.page.screenshot(),name="content loaded after few seconds",attachment_type=AttachmentType.PNG)

    def validate_alertpresent(self):
         expect(self.alert_button).to_be_visible()
         allure.attach(self.page.screenshot(),name="alert button is visible",attachment_type=AttachmentType.PNG)

         alert_message = ""

         def handle_dialog(dialog):
             nonlocal alert_message
             alert_message = dialog.message
             print("Alert content:", alert_message)
             dialog.accept()

         self.page.on("dialog", handle_dialog)
         try:
             self.alert_button.click(timeout=15000)
         except Exception:
             pass
         finally:
             self.page.remove_listener("dialog", handle_dialog)

         return alert_message

    def validate_prompt(self):
         expect(self.prompt_button).to_be_visible()
         allure.attach(self.page.screenshot(),name="promt button is visible",attachment_type=AttachmentType.PNG)

         def handle_prompt(dialog):
                dialog.accept("test")

         self.page.on("dialog",handle_prompt)
         try:
              self.prompt_button.click()
              allure.attach(self.page.screenshot(),name="promt is visible",attachment_type=AttachmentType.PNG)
              
         except Exception:
              pass
         finally:
              self.page.remove_listener("dialog",handle_prompt)
         

         
              

         

      




        