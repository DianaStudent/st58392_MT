import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/login")
        self.wait = WebDriverWait(self.driver, 20)

    def test_elements_presence(self):
        try:
            # Verify headers
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header.header-area")))

            # Verify navigation links
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))

            # Verify account buttons
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))

            # Verify login form elements
            self.wait.until(EC.visibility_of_element_located((By.NAME, "email")))
            self.wait.until(EC.visibility_of_element_located((By.NAME, "password")))
            self.wait.until(EC.visibility_of_element_located((By.NAME, "repeatPassword")))
            self.wait.until(EC.visibility_of_element_located((By.NAME, "firstName")))
            self.wait.until(EC.visibility_of_element_located((By.NAME, "lastName")))
            self.wait.until(EC.visibility_of_element_located((By.NAME, "stateProvince")))

            # Verify buttons
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[aria-label='Accept cookies']")))
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))

            # Verify footer
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer.footer-area")))
        
        except Exception as e:
            self.fail(f"A required element was not found or visible: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()