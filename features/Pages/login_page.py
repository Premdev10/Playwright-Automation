from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        
        # Locators
        self.username_input = page.locator('//input[@id="login-username"]')
        self.password_input = page.locator('//input[@id="login-password"]')
        self.captcha_checkbox=page.locator('//input[@data-testid="login-captcha-toggle"]')
        self.login_button = page.locator('//button[@type="submit"]')
        self.atptitle = page.locator('//p[contains(text(), "Automation Testing Playground")]')
        self.pagetitle = page.locator('//div//h2')
        self.otpbox=page.locator('//input[@id="otp-input"]')
        self.otpverify=page.locator('//button[text()="Verify"]')

    # Methods / Actions

    def goto_loginpage(self):
        self.page.goto("file:///C:/Users/premd/Downloads/automation-testing-playground-pro_1.html")
        expect(self.atptitle).to_be_visible()

    def goto_respective_page(self,url):
        self.page.goto(url)


    def enter_credentials(self, username, password):
        """Fills in the username and password fields."""
        self.username_input.fill(username)
        self.password_input.fill(password)

    def click_login(self):
        """Clicks the login button."""
        self.captcha_checkbox.click()  # Check the captcha checkbox
        self.login_button.click()

    def enter_otp(self, otp):
        self.otpbox.fill(otp)
        self.otpverify.click()

    def verify_dashboard_redirect(self):
        """Waits for the page title to become visible and verifies the dashboard."""
        self.pagetitle.wait_for()
        if self.pagetitle.is_visible():
            print("User is redirected to the dashboard successfully.")
            pagetitle_text=self.pagetitle.text_content()
            if pagetitle_text.__contains__("Welcome back,"):
                print("dashboard has proper title")
            else:
                print("dashboard title is not proper")

        else:
            print("Failed to redirect to the dashboard.")

 

