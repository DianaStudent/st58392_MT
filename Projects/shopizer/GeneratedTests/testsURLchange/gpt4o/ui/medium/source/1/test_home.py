import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class ShopizerUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_key_ui_elements(self):
        driver = self.driver
        driver.get("http://localhost/")

        # Check presence of header navigation links
        try:
            home_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            tables_link = driver.find_element(By.LINK_TEXT, "Tables")
            chairs_link = driver.find_element(By.LINK_TEXT, "Chairs")
        except Exception as e:
            self.fail(f"Navigation link element missing: {str(e)}")

        # Check presence of buttons and interactive elements
        try:
            accept_cookies_button = self.wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            shop_now_button = driver.find_element(By.LINK_TEXT, "Shop Now")
        except Exception as e:
            self.fail(f"Button element missing: {str(e)}")

        # Interact with a button and check UI updates
        try:
            accept_cookies_button.click()  # Clicking on the accept cookies button
        except Exception as e:
            self.fail(f"Button interaction failed: {str(e)}")

        # Check presence of form elements
        try:
            email_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "email")))
            subscribe_button = driver.find_element(By.CSS_SELECTOR, "button.button")
        except Exception as e:
            self.fail(f"Form element missing: {str(e)}")

        # Verify banner presence
        try:
            promo_image = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@alt='promo20']")))
        except Exception as e:
            self.fail(f"Banner element missing: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()