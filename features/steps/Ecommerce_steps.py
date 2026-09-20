from behave import given, when, then, step
from utils.excel_reader import ExcelReader
from Pages.Ecommerce_page import Ecommercepage


@then('user clicks on ecommerce tab')
def step_impl(context):
    ecommerce_page = Ecommercepage(context.page)
    ecommerce_page.validate_ecommercetab()

@then('validate user navigated in to the shop section')
def validate_shopsection(context):
    ecommerce_page = Ecommercepage(context.page)
    ecommerce_page.validate_shoptab()

@then('validate user able to add the product "{productname}" in to the cart')
def validate_addtocart(context,productname):
    ecommerce_page = Ecommercepage(context.page)
    ecommerce_page.validate_addtocart(productname)

@then('user clicks on banking button')
def click_banking_link(context):
    ecommerce_page = Ecommercepage(context.page)
    ecommerce_page.click_banking_link()

@then('user clicks on the transfer money link')
def click_transfer_money(context):
     ecommerce_page = Ecommercepage(context.page)
     ecommerce_page.click_transfer_link()

@then('verify user should be able to transfer the money')
def verify_transfer_money(context):
    ecommerce_page = Ecommercepage(context.page)
    ecommerce_page.verify_transfer_amount()

@then('user clicks on the transaction history tab')
def click_trans_his_tab(context):
    ecommerce_page = Ecommercepage(context.page)
    ecommerce_page.click_trans_his_tab()

@then('verify the transaction is available in the table')
def verify_transaction_table(context):
    ecommerce_page = Ecommercepage(context.page)
    ecommerce_page.verify_transaction_()

@then('user clicks on the beneficiary tab')
def click_beneficiary(context):
    ecommerce_page = Ecommercepage(context.page)
    ecommerce_page.click_beneficiary_tab()

@then('verify able to add the beneficiary')
def verify_add_beneficiary(context):
    ecommerce_page = Ecommercepage(context.page)
    ecommerce_page.add_beneficiary_success()

@then('verify beneficiary available in the table')
def verify_bene_table(context):
    ecommerce_page = Ecommercepage(context.page)
    ecommerce_page.verify_ben_table()