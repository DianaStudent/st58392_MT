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
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Verify header is visible
        header = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header.header-area")))
        self.assertIsNotNone(header, "Header is not visible")

        # Verify footer is visible
        footer = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer.footer-area")))
        self.assertIsNotNone(footer, "Footer is not visible")

        # Validate presence of navigation links
        nav_links = ["Home", "Tables", "Chairs"]
        for link in nav_links:
            nav_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link)))
            self.assertIsNotNone(nav_link, f"{link} link is not visible")

        # Check login/register tab is present
        login_tab = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@data-rb-event-key='login']")))
        register_tab = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@data-rb-event-key='register']")))
        self.assertIsNotNone(login_tab, "Login tab is not visible")
        self.assertIsNotNone(register_tab, "Register tab is not visible")

        # Check input fields on the registration form
        input_fields = [
            ("name", "email"),
            ("name", "password"),
            ("name", "repeatPassword"),
            ("name", "firstName"),
            ("name", "lastName"),
            ("name", "stateProvince"),
        ]
        for attribute, value in input_fields:
            input_field = self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//input[@{attribute}='{value}']")))
            self.assertIsNotNone(input_field, f"Input field {value} is not visible")

        # Check register button
        register_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button/span[text()='Register']")))
        self.assertIsNotNone(register_button, "Register button is not visible")

        # Interact with the accept cookies button
        accept_cookies_button = self.wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
        accept_cookies_button.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()