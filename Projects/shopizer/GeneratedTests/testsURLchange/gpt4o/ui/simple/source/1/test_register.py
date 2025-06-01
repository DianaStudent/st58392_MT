import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/login")

    def test_page_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check for logo visibility
        try:
            logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.logo img")))
        except:
            self.fail("Logo not found or not visible.")

        # Check main menu links
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            tables_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            chairs_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
        except:
            self.fail("Main menu links not found or not visible.")

        # Check login form fields
        try:
            wait.until(EC.visibility_of_element_located((By.NAME, "email")))
            wait.until(EC.visibility_of_element_located((By.NAME, "password")))
            wait.until(EC.visibility_of_element_located((By.NAME, "repeatPassword")))
            wait.until(EC.visibility_of_element_located((By.NAME, "firstName")))
            wait.until(EC.visibility_of_element_located((By.NAME, "lastName")))
        except:
            self.fail("Form fields not found or not visible.")

        # Check buttons
        try:
            login_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button/span[text()='Register']")))
            accept_cookies_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
        except:
            self.fail("Buttons not found or not visible.")

        # Additional elements (language dropdown, cart icon, footer)
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "same-language-currency")))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "icon-cart")))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer-area")))
        except:
            self.fail("Additional elements not found or not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()