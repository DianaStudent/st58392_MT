import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class ShopizerUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/login")
        self.wait = WebDriverWait(self.driver, 20)

    def test_UI_elements(self):
        driver = self.driver

        # Check header
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-area")))
        except:
            self.fail("Header not found or not visible")

        # Check main menu links
        try:
            home_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            tables_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            chairs_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
        except:
            self.fail("Main menu links are missing or not visible")

        # Check login form elements
        try:
            email_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "email")))
            password_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "loginPassword")))
            login_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button/span[text()='Login']/..")))
        except:
            self.fail("Login form elements are missing or not visible")

        # Interact with Cookie consent
        try:
            cookie_button = self.wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            cookie_button.click()
        except:
            self.fail("Cookie consent button is missing or not clickable")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()