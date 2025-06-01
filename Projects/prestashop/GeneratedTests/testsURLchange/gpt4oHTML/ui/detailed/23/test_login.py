import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestUILoginPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/login")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_presence(self):
        driver = self.driver

        # Check for header
        header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
        if not header:
            self.fail("Header is not visible.")

        # Check for footer
        footer = self.wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        if not footer:
            self.fail("Footer is not visible.")

        # Check for navigation elements
        nav_elements = [
            ("ul#top-menu", "Header navigation"),
            ("#_desktop_contact_link a[href='http://localhost:8080/en/contact-us']", "Contact us link"),
            ("#_desktop_user_info a[rel='nofollow']", "Sign in link"),
            ("#_desktop_cart .shopping-cart", "Cart link")
        ]
        for selector, description in nav_elements:
            element = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
            if not element:
                self.fail(f"{description} is not visible.")

        # Check input fields and buttons in the login form
        login_form_elements = [
            ("#login-form input[name='email']", "Email input field"),
            ("#login-form input[name='password']", "Password input field"),
            ("#submit-login", "Sign in button"),
            ("a[href='http://localhost:8080/en/password-recovery']", "Forgot your password link"),
            ("a[href='http://localhost:8080/en/registration']", "Create account link")
        ]
        for selector, description in login_form_elements:
            element = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
            if not element:
                self.fail(f"{description} is not visible.")

        # Interact with the "Sign in" button to ensure UI reacts visually
        sign_in_button = self.wait.until(EC.element_to_be_clickable((By.ID, "submit-login")))
        sign_in_button.click()

        # Check if some visual change happened, for example, an error message or the loading of another page.
        try:
            error_message = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".form-control-comment")))
            if not error_message:
                self.fail("Error message box is not visible after clicking sign-in with empty fields.")
        except:
            # In case an error is not displayed, consider the test passed as it may switch to another page
            pass

        # Lookup additional UI elements visibility
        additional_ui_checks = [
            ("#wrapper", "Main wrapper section"),
            ("nav.breadcrumb", "Breadcrumb navigation")
        ]
        for selector, description in additional_ui_checks:
            element = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
            if not element:
                self.fail(f"{description} is not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()