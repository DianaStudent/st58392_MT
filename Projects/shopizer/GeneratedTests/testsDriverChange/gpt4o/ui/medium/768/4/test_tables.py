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
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_ui_elements(self):
        driver = self.driver

        # Verify key UI elements
        try:
            # Header and Logo
            header = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-area")))
            logo = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".logo img")))

            # Navigation Links
            home_link = driver.find_element(By.LINK_TEXT, "Home")
            tables_link = driver.find_element(By.LINK_TEXT, "Tables")
            chairs_link = driver.find_element(By.LINK_TEXT, "Chairs")

            # Main content and products
            product_grid = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "grid")))

            # Buttons
            accept_cookies_button = self.wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))

            # Form fields and footer
            subscribe_email = driver.find_element(By.NAME, "email")
            subscribe_button = driver.find_element(By.CSS_SELECTOR, ".subscribe-style .button")

            # Verify visibility
            self.assertTrue(header.is_displayed())
            self.assertTrue(logo.is_displayed())
            self.assertTrue(home_link.is_displayed())
            self.assertTrue(tables_link.is_displayed())
            self.assertTrue(chairs_link.is_displayed())
            self.assertTrue(product_grid.is_displayed())
            self.assertTrue(accept_cookies_button.is_displayed())
            self.assertTrue(subscribe_email.is_displayed())
            self.assertTrue(subscribe_button.is_displayed())

            # Interact with elements
            accept_cookies_button.click()
            self.wait.until(EC.invisibility_of_element(accept_cookies_button))

        except Exception as e:
            self.fail(f"UI element check failed: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()