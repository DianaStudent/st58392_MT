import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestUIProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Verify key structural elements are present and visible
        # Verify header
        header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'header.header-area')))
        self.assertIsNotNone(header, "Header is not visible.")
        
        # Verify footer
        footer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'footer.footer-area')))
        self.assertIsNotNone(footer, "Footer is not visible.")
        
        # Verify main menu
        nav_home = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Home')))
        nav_tables = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Tables')))
        nav_chairs = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Chairs')))

        self.assertIsNotNone(nav_home, "Home link is not visible.")
        self.assertIsNotNone(nav_tables, "Tables link is not visible.")
        self.assertIsNotNone(nav_chairs, "Chairs link is not visible.")
        
        # Check visibility of accept cookies button
        accept_cookies_btn = wait.until(EC.visibility_of_element_located((By.ID, 'rcc-confirm-button')))
        self.assertIsNotNone(accept_cookies_btn, "Accept cookies button is not visible.")
        
        # Interact with accept cookies button
        accept_cookies_btn.click()
        
        # Navigate to register page and ensure elements are visible
        driver.get("http://localhost/register")
        
        # Verify register page elements
        email_input = wait.until(EC.visibility_of_element_located((By.NAME, 'email')))
        password_input = wait.until(EC.visibility_of_element_located((By.NAME, 'password')))
        repeat_password_input = wait.until(EC.visibility_of_element_located((By.NAME, 'repeatPassword')))
        first_name_input = wait.until(EC.visibility_of_element_located((By.NAME, 'firstName')))
        last_name_input = wait.until(EC.visibility_of_element_located((By.NAME, 'lastName')))
        state_input = wait.until(EC.visibility_of_element_located((By.NAME, 'stateProvince')))
        register_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))

        self.assertIsNotNone(email_input, "Email input is not visible.")
        self.assertIsNotNone(password_input, "Password input is not visible.")
        self.assertIsNotNone(repeat_password_input, "Repeat password input is not visible.")
        self.assertIsNotNone(first_name_input, "First name input is not visible.")
        self.assertIsNotNone(last_name_input, "Last name input is not visible.")
        self.assertIsNotNone(state_input, "State input is not visible.")
        self.assertIsNotNone(register_button, "Register button is not visible.")
        
        # Assert that there are no missing elements
        all_elements = [
            header, footer,
            nav_home, nav_tables, nav_chairs,
            accept_cookies_btn,
            email_input, password_input, repeat_password_input,
            first_name_input, last_name_input, state_input, register_button
        ]
        
        for element in all_elements:
            self.assertTrue(element.is_displayed(), f"An element is not visible: {element}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()