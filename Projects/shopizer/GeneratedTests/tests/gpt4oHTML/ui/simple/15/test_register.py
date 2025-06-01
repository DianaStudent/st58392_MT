import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_components(self):
        driver = self.driver
        wait = self.wait

        # Check Header Components
        try:
            logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".logo a img")))
        except:
            self.fail("Logo is missing.")

        try:
            nav_home = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
        except:
            self.fail("'Home' link is missing from navigation.")

        try:
            nav_tables = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
        except:
            self.fail("'Tables' link is missing from navigation.")

        try:
            nav_chairs = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
        except:
            self.fail("'Chairs' link is missing from navigation.")

        try:
            nav_login = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
        except:
            self.fail("'Login' link is missing from navigation.")

        try:
            nav_register = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
        except:
            self.fail("'Register' link is missing from navigation.")

        # Check Cookie Consent Button
        try:
            cookie_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
        except:
            self.fail("Cookie consent button is missing.")

        # Test Register Form Fields' visibility
        driver.get("http://localhost/register")
        try:
            email_input = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
        except:
            self.fail("Email input is missing on registration.")

        try:
            password_input = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
        except:
            self.fail("Password input is missing on registration.")

        try:
            repeat_password_input = wait.until(EC.visibility_of_element_located((By.NAME, "repeatPassword")))
        except:
            self.fail("Repeat Password input is missing on registration.")

        try:
            first_name_input = wait.until(EC.visibility_of_element_located((By.NAME, "firstName")))
        except:
            self.fail("First Name input is missing on registration.")

        try:
            last_name_input = wait.until(EC.visibility_of_element_located((By.NAME, "lastName")))
        except:
            self.fail("Last Name input is missing on registration.")

        # Check if Country Select Exists
        try:
            country_select = wait.until(EC.visibility_of_element_located((By.XPATH, "//select[option/text()='Select a country']")))
        except:
            self.fail("Country select dropdown is missing on registration.")

        # Check if State/Province Input Exists
        try:
            state_input = wait.until(EC.visibility_of_element_located((By.NAME, "stateProvince")))
        except:
            self.fail("State/Province input is missing on registration.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()