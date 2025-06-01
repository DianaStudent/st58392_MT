from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/register?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check for navigation links
        nav_links = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-links")))
        self.assertIsNotNone(nav_links, "Navigation links are missing.")

        # Check for Register button in navigation
        register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
        self.assertIsNotNone(register_link, "Register link is missing.")

        # Check for login button/input
        login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Log in")))
        self.assertIsNotNone(login_link, "Login link is missing.")

        # Confirm presence of search input
        search_input = wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
        self.assertIsNotNone(search_input, "Search input is missing.")

        # Interacting with elements: Click Register button
        register_link.click()

        # Check Register page fields
        first_name_input = wait.until(EC.visibility_of_element_located((By.ID, "FirstName")))
        last_name_input = wait.until(EC.visibility_of_element_located((By.ID, "LastName")))
        email_input = wait.until(EC.visibility_of_element_located((By.ID, "Email")))
        password_input = wait.until(EC.visibility_of_element_located((By.ID, "Password")))
        register_button = wait.until(EC.visibility_of_element_located((By.ID, "register-button")))

        elements = [first_name_input, last_name_input, email_input, password_input, register_button]
        
        for element in elements:
            if not (element and element.is_displayed()):
                self.fail(f"One of the registration page elements is missing or not visible: {element}")

        # UI update check
        first_name_input.send_keys("Test")
        last_name_input.send_keys("User")
        email_input.send_keys("testuser@example.com")
        password_input.send_keys("Password123")
        
        # Verify no errors present when interacting with UI
        try:
            register_button.click()
            success_notification = wait.until(
                EC.visibility_of_element_located((By.ID, "dialog-notifications-success"))
            )
            self.assertIsNotNone(success_notification, "Success notification is missing or not visible.")
        except:
            self.fail("Interacting with the UI caused an error.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()