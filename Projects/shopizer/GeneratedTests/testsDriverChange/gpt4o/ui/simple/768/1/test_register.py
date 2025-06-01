from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestUIElements(unittest.TestCase):

    def setUp(self):
        # Setup Chrome WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def test_page_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header elements
        try:
            header_logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".logo img")))
            self.assertTrue(header_logo.is_displayed())
        except:
            self.fail("Header logo not found or not visible")

        # Check main menu navigation links
        try:
            nav_home = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            nav_tables = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            nav_chairs = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
            self.assertTrue(nav_home.is_displayed())
            self.assertTrue(nav_tables.is_displayed())
            self.assertTrue(nav_chairs.is_displayed())
        except:
            self.fail("Main navigation links not found or not visible")

        # Check footer elements
        try:
            footer_logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".footer-logo img")))
            subscribe_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".button")))
            self.assertTrue(footer_logo.is_displayed())
            self.assertTrue(subscribe_button.is_displayed())
        except:
            self.fail("Footer elements not found or not visible")

        # Check login/register form
        driver.get("http://localhost/login")
        try:
            login_tab = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@data-rb-event-key='login']")))
            register_tab = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@data-rb-event-key='register']")))
            self.assertTrue(login_tab.is_displayed())
            self.assertTrue(register_tab.is_displayed())
        except:
            self.fail("Login/Register tabs not found or not visible")

        # Check form fields
        try:
            email_input = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
            password_input = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
            repeat_password_input = wait.until(EC.visibility_of_element_located((By.NAME, "repeatPassword")))
            register_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button/span[text()='Register']")))
            self.assertTrue(email_input.is_displayed())
            self.assertTrue(password_input.is_displayed())
            self.assertTrue(repeat_password_input.is_displayed())
            self.assertTrue(register_button.is_displayed())
        except:
            self.fail("Form fields not found or not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()