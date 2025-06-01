import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebpageUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check header elements
        try:
            logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".logo a img")))
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            tables_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            chairs_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
        except Exception as e:
            self.fail(f"Header elements not found or not visible: {e}")

        # Check for the cookie consent button
        try:
            cookie_consent_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
        except Exception as e:
            self.fail(f"Cookie consent button not found or not visible: {e}")

        # Check for 'Featured Products' section
        try:
            featured_products = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".section-title-5")))
            olive_table = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Olive Table")))
            genuine_chair = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Genuine Chair")))
        except Exception as e:
            self.fail(f"Featured Products section elements not found or not visible: {e}")

        # Check for footer elements
        try:
            contact_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Contact")))
            login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
            register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
        except Exception as e:
            self.fail(f"Footer elements not found or not visible: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()