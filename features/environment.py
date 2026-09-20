import allure
from playwright.sync_api import sync_playwright
from utils.config_reader import ConfigReader

def before_all(context):
    context.playwright = sync_playwright().start()
    
    browser_type = ConfigReader.get_config_value('Environment', 'browser')
    headless_mode = ConfigReader.get_config_value('Environment', 'headless') == 'True'
    
    if browser_type.lower() == 'firefox':
        context.browser = context.playwright.firefox.launch(headless=headless_mode)
    elif browser_type.lower() == 'webkit':
        context.browser = context.playwright.webkit.launch(headless=headless_mode)
    else:
        context.browser = context.playwright.chromium.launch(headless=headless_mode)

def before_scenario(context, scenario):
    context.page = context.browser.new_page()

def after_scenario(context, scenario):
    if scenario.status == "failed":
        try:
            screenshot = context.page.screenshot(full_page=True)
            allure.attach(
                screenshot,
                name=f"Failed_{scenario.name}",
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print(f"Failed to capture screenshot: {e}")
            
    context.page.close()

def after_all(context):
    context.browser.close()
    context.playwright.stop()
