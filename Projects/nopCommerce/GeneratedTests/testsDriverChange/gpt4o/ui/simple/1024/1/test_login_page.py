import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class WebsiteUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/login?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_present(self):
        # Checking header links
        headers = [
            ("Register", "/register?returnUrl=%2F"),
            ("Log in", "/login?returnUrl=%2F"),
            ("Wishlist", "/wishlist"),
            ("Shopping cart", "/cart")
        ]

        for label, link in headers:
            element = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, label)))
            self.assertTrue(element.is_displayed(), f"{label} link not visible")
            self.assertEqual(element.get_attribute("href"), f"http://max{link}", f"{label} link href mismatch")

        # Checking footer links
        footer_links = [
            "Sitemap", "Shipping & returns", "Privacy notice", "Conditions of Use", 
            "About us", "Contact us", "Search", "News", "Blog", "Recently viewed products", 
            "Compare products list", "New products", "Orders", "Addresses", "Shopping cart", 
            "Wishlist", "Apply for vendor account"
        ]

        for link in footer_links:
            element = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link)))
            self.assertTrue(element.is_displayed(), f"{link} link not visible")

        # Checking main content
        page_title = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1")))
        self.assertEqual(page_title.text, "Welcome, Please Sign In!", "Page title mismatch")

        # Checking form fields
        email_field = self.wait.until(EC.visibility_of_element_located((By.ID, "Email")))
        self.assertTrue(email_field.is_displayed(), "Email field not visible")

        password_field = self.wait.until(EC.visibility_of_element_located((By.ID, "Password")))
        self.assertTrue(password_field.is_displayed(), "Password field not visible")

        login_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.login-button")))
        self.assertTrue(login_button.is_displayed(), "Login button not visible")

        remember_me_checkbox = self.wait.until(EC.visibility_of_element_located((By.ID, "RememberMe")))
        self.assertTrue(remember_me_checkbox.is_displayed(), "Remember me checkbox not visible")

        forgot_password_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Forgot password?")))
        self.assertTrue(forgot_password_link.is_displayed(), "Forgot password link not visible")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()