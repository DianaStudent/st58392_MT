import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check header
        try:
            header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".header-area")))
        except:
            self.fail("Header is missing or not visible.")

        # Check footer
        try:
            footer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".footer-area")))
        except:
            self.fail("Footer is missing or not visible.")

        # Check navigation links
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            tables_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            chairs_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
        except:
            self.fail("Navigation links are missing or not visible.")

        # Check cookie consent button
        try:
            cookie_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            cookie_button.click()
        except:
            self.fail("Cookie consent button is missing or not visible.")

        # Check login and register buttons
        try:
            login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
            register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
        except:
            self.fail("Login/Register links are missing or not visible.")

        # Check subscription input and button
        try:
            subscribe_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".subscribe-form .email")))
            subscribe_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".subscribe-form .button")))
        except:
            self.fail("Subscription form is missing or not visible.")

        # Check featured products section
        try:
            featured_products = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-area")))
        except:
            self.fail("Featured products section is missing or not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()