import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestWebElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Verify header logo
        try:
            logo = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".logo img"))
            )
        except:
            self.fail("Logo not found or not visible")

        # Verify main menu links
        try:
            home_link = self.wait.until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Home"))
            )
            tables_link = self.wait.until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Tables"))
            )
            chairs_link = self.wait.until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Chairs"))
            )
        except:
            self.fail("Main menu links not found or not visible")

        # Verify buttons in cookie consent
        try:
            cookie_button = self.wait.until(
                EC.visibility_of_element_located((By.ID, "rcc-confirm-button"))
            )
        except:
            self.fail("Cookie consent button not found or not visible")

        # Verify account actions
        try:
            account_button = self.wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "account-setting-active"))
            )
        except:
            self.fail("Account button not found or not visible")

        # Verify cart icon
        try:
            cart_icon = self.wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "icon-cart"))
            )
        except:
            self.fail("Cart icon not found or not visible")

        # Verify subscribe form
        try:
            subscribe_input = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".subscribe-area-3 .email"))
            )
            subscribe_button = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".subscribe-area-3 .button"))
            )
        except:
            self.fail("Subscribe form not found or not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()