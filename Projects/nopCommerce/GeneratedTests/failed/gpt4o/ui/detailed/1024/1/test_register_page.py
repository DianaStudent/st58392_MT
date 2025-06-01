from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class NopCommerceUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)
        self.base_url = "http://max/register?returnUrl=%2F"

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        driver = self.driver
        driver.get(self.base_url)

        # Verify header is present and visible
        header = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
        if not header:
            self.fail("Header is not visible")

        # Verify footer is present and visible
        footer = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))
        if not footer:
            self.fail("Footer is not visible")

        # Verify registration form elements
        self.check_element_visible(By.ID, "FirstName", "First name input")
        self.check_element_visible(By.ID, "LastName", "Last name input")
        self.check_element_visible(By.ID, "Email", "Email input")
        self.check_element_visible(By.ID, "Password", "Password input")
        self.check_element_visible(By.ID, "ConfirmPassword", "Confirm password input")
        self.check_element_visible(By.ID, "register-button", "Register button")

        # Verify header menu links
        self.check_link_visible(By.LINK_TEXT, "Home page")
        self.check_link_visible(By.LINK_TEXT, "New products")
        self.check_link_visible(By.LINK_TEXT, "My account")
        self.check_link_visible(By.LINK_TEXT, "Blog")
        self.check_link_visible(By.LINK_TEXT, "Contact us")

        # Verify interaction with Register button
        register_button = driver.find_element(By.ID, "register-button")
        register_button.click()
        
        # Confirm UI reaction
        alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
        if not alert:
            self.fail("No alert appeared after clicking Register button")

    def check_element_visible(self, by, value, name):
        element = self.wait.until(EC.visibility_of_element_located((by, value)))
        if not element:
            self.fail(f"{name} is not visible")

    def check_link_visible(self, by, value):
        link = self.wait.until(EC.visibility_of_element_located((by, value)))
        if not link:
            self.fail(f"Link with {by}: '{value}' is not visible")

if __name__ == "__main__":
    unittest.main()