import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestRegisterPageUI(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/register?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check visibility of structural elements
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))
        except:
            self.fail("Header or Footer is not visible")

        # Check main navigation links
        nav_links = [
            (By.LINK_TEXT, "Home page"),
            (By.LINK_TEXT, "New products"),
            (By.LINK_TEXT, "Search"),
            (By.LINK_TEXT, "My account"),
            (By.LINK_TEXT, "Blog"),
            (By.LINK_TEXT, "Contact us")
        ]

        for link in nav_links:
            try:
                wait.until(EC.visibility_of_element_located(link))
            except:
                self.fail(f"Navigation link {link} is not visible")

        # Check presence and visibility of form fields and sections
        form_elements = [
            (By.ID, "FirstName"),
            (By.ID, "LastName"),
            (By.ID, "Email"),
            (By.ID, "Password"),
            (By.ID, "ConfirmPassword"),
            (By.ID, "register-button")
        ]

        for element in form_elements:
            try:
                wait.until(EC.visibility_of_element_located(element))
            except:
                self.fail(f"Form element {element} is not visible")

        # Interact with 'Register' button
        try:
            register_button = wait.until(EC.element_to_be_clickable((By.ID, "register-button")))
            register_button.click()
        except:
            self.fail("Register button is not clickable or not visible")

        # Check for error notifications after clicking Register
        try:
            wait.until(EC.visibility_of_element_located((By.ID, "dialog-notifications-error")))
        except:
            self.fail("Error notification is not visible after submitting form")

if __name__ == "__main__":
    unittest.main()