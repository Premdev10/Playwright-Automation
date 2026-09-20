from playwright.sync_api import Page, expect
import allure
from allure_commons.types import AttachmentType

class Ecommercepage:
    beneficiary_name="Rahul"

    def __init__(self, page: Page):
        self.page = page


        



        #locators
        self.ecommerce_button=page.locator("//h3[text()='E-Commerce']")
        self.shop_title=page.get_by_role("button",name="Shop")
        self.addtocart_button=page.locator('//button[@data-testid="open-cart-btn"]')
        self.subtotal_text=page.locator("//span[text()='Subtotal']")
        self.proceed_checkout=page.get_by_role("button",name="Proceed to checkout")
        self.firstname=page.get_by_test_id("checkout-name-input")
        self.zipcode=page.get_by_test_id("checkout-zip-input")
        self.addline=page.get_by_test_id("checkout-address-input")
        self.city=page.get_by_test_id("checkout-city-input")
        self.continue_payment_button=page.get_by_role("button",name="Continue to payment")
        self.cardnumber=page.get_by_test_id("card-number-input")
        self.expirydate=page.get_by_test_id("card-expiry-input")
        self.placeorder=page.get_by_role("button",name="Place order")
        self.banking_icon=page.get_by_test_id("nav-banking")
        self.transfer_link=page.get_by_test_id("tab-transfer")
        self.transfer_dropdown=page.locator('//select[@id="transfer-beneficiary"]')
        self.amount_payable=page.get_by_test_id("transfer-amount-input")
        self.transfer_but=page.get_by_test_id("transfer-submit-btn")
        self.otp_transfer=page.get_by_test_id("transfer-otp-input")
        self.otp_confirm_transfer=page.get_by_test_id("transfer-otp-confirm-btn")
        self.trans_his_tab=page.get_by_test_id("tab-transactions")
        self.table_transaction=page.get_by_test_id("transactions-table")
        self.table_headers=page.locator('//table[@data-testid="transactions-table"]//thead//th')
        self.beneficiary_tab=page.get_by_test_id("tab-beneficiaries")
        self.add_beneficiary=page.get_by_test_id("add-beneficiary-btn")
        self.ben_name=page.get_by_test_id("beneficiary-name-input")
        self.ben_account=page.get_by_test_id("beneficiary-account-input")
        self.ben_ifsc=page.get_by_test_id("beneficiary-ifsc-input")
        self.bank=page.get_by_test_id("beneficiary-bank-input")
        self.save_ben_button=page.get_by_test_id("beneficiary-save-btn")
        

        


    def validate_ecommercetab(self):
            expect(self.ecommerce_button).to_be_visible()
            self.ecommerce_button.click()
            

    def validate_shoptab(self):
         expect(self.shop_title).to_be_visible()

    def validate_addtocart(self,productname):
          self.product_name=self.page.locator("(//div//h4[text()='"+productname+"']//following::button[text()='Add to cart'])[1]")
          self.product_name.click()
          self.addtocart_button.click()
          expect(self.subtotal_text).to_be_visible()
          self.proceed_checkout.click()
          expect(self.firstname).to_be_visible()
          self.firstname.clear()
          self.firstname.fill("rahul")
          self.zipcode.clear()
          self.zipcode.fill("679514")
          self.addline.clear()
          self.addline.fill("test 1234")
          self.city.clear()
          self.city.fill("kochi")
          allure.attach(self.page.screenshot(),name="address details added",attachment_type=AttachmentType.PNG)
          self.continue_payment_button.click()
          expect(self.cardnumber).to_be_visible()
          self.cardnumber.fill("123412341234")
          self.expirydate.fill("10/29")
          self.placeorder.click()
          allure.attach(self.page.screenshot(),name="order placed successfully",attachment_type=AttachmentType.PNG)

    def click_banking_link(self):
         expect(self.banking_icon).to_be_visible()
         self.banking_icon.click()

    def click_transfer_link(self):
         expect(self.transfer_link).to_be_visible()
         self.transfer_link.click()

    def verify_transfer_amount(self):
         expect(self.transfer_dropdown).to_be_visible()
         self.transfer_dropdown.select_option(value="B-2")
         self.amount_payable.fill("100")
         allure.attach(self.page.screenshot(),name="details entered",attachment_type=AttachmentType.PNG)
         self.transfer_but.click()
         expect(self.otp_transfer).to_be_visible()
         self.otp_transfer.fill("123456")
         self.otp_confirm_transfer.click()
         expect(self.transfer_link).to_be_visible()
         self.page.wait_for_timeout(5000)
         allure.attach(self.page.screenshot(),name="amount transfered successfully",attachment_type=AttachmentType.PNG)

    def click_trans_his_tab(self):
         expect(self.trans_his_tab).to_be_visible()
         self.trans_his_tab.click()

    def verify_transaction_(self):
         expected_headers=['ID', 'Date', 'Type', 'Party', 'Amount', 'Status']
         expect(self.table_transaction).to_be_visible()
         actual_headers=[h.strip() for h in self.table_headers.all_text_contents()]
         allure.attach(str(actual_headers), name="actual_headers", attachment_type=AttachmentType.TEXT)
         print(f"extracted headers:",actual_headers)
         assert actual_headers==expected_headers,f"expected {expected_headers},but got {actual_headers}"
         allure.attach(self.page.screenshot(),name="transaction table headers",attachment_type=AttachmentType.PNG)

    def click_beneficiary_tab(self):
         expect(self.beneficiary_tab).to_be_visible()
         self.beneficiary_tab.click()
         expect(self.add_beneficiary).to_be_visible()

    def add_beneficiary_success(self):
         self.add_beneficiary.click()
         expect(self.ben_name).to_be_visible()
         self.ben_name.fill(self.beneficiary_name)
         self.ben_account.fill("savings")
         self.ben_ifsc.fill("IFCTEST1111")
         self.bank.fill("ICICI")
         self.save_ben_button.click()

    def verify_ben_table(self):
         beneficiary_cell = self.page.locator(
             "//table[@data-testid='beneficiaries-table']//tr//td[text()='" + self.beneficiary_name + "']"
         )
         expect(beneficiary_cell).to_be_visible()
         allure.attach(self.page.screenshot(), name="beneficiary row visible", attachment_type=AttachmentType.PNG)
         
         

         

              
         
          



         
         
                 
