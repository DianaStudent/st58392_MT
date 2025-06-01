import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        driver = self.driver

        # Define a wait instance with a timeout of 20 seconds
        wait = WebDriverWait(driver, 20)

        # Check the visibility of the header
        header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header.header-area")))
        self.assertTrue(header.is_displayed(), "Header is not visible")

        # Check the visibility of the footer
        footer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer.footer-area")))
        self.assertTrue(footer.is_displayed(), "Footer is not visible")

        # Check main navigation links
        nav_home = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
        nav_tables = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
        nav_chairs = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))

        self.assertTrue(nav_home.is_displayed(), "Home link is not visible")
        self.assertTrue(nav_tables.is_displayed(), "Tables link is not visible")
        self.assertTrue(nav_chairs.is_displayed(), "Chairs link is not visible")

        # Interact with Accept Cookies button if present
        try:
            accept_cookies = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            accept_cookies.click()
        except:
            self.fail("Accept Cookies button is not present or not clickable")

        # Navigate to register page and verify form fields
        driver.get("http://localhost/register")

        email_input = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
        password_input = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
        repeat_password_input = wait.until(EC.visibility_of_element_located((By.NAME, "repeatPassword")))
        first_name_input = wait.until(EC.visibility_of_element_located((By.NAME, "firstName")))
        last_name_input = wait.until(EC.visibility_of_element_located((By.NAME, "lastName")))
        country_select = wait.until(EC.visibility_of_element_located((By.XPATH, "//select[option='Select a country']")))
        
        # Assert the visibility of input fields
        self.assertTrue(email_input.is_displayed(), "Email input field is not visible")
        self.assertTrue(password_input.is_displayed(), "Password input field is not visible")
        self.assertTrue(repeat_password_input.is_displayed(), "Repeat Password input field is not visible")
        self.assertTrue(first_name_input.is_displayed(), "First Name input field is not visible")
        self.assertTrue(last_name_input.is_displayed(), "Last Name input field is not visible")
        self.assertTrue(country_select.is_displayed(), "Country select box is not visible")

        # Verify Register button
        register_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[span='Register']")))
        self.assertTrue(register_button.is_displayed(), "Register button is not visible")

if __name__ == "__main__":
    unittest.main()