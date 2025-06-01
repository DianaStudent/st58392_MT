import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check header logo
        try:
            self.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".logo a img")))
        except:
            self.fail("Logo is not visible on the page")

        # Check top navigation menu
        try:
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
        except:
            self.fail("Top navigation menu items are not visible on the page")

        # Check account setting button
        try:
            self.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".account-setting-active")))
        except:
            self.fail("Account setting button is not visible on the page")

        # Check cart button
        try:
            self.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".cart-wrap button.icon-cart")))
        except:
            self.fail("Cart button is not visible on the page")

        # Check "Accept cookies" button
        try:
            self.wait.until(EC.visibility_of_element_located(
                (By.ID, "rcc-confirm-button")))
        except:
            self.fail("Accept cookies button is not visible on the page")

        # Check featured products
        try:
            self.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".product-area")))
        except:
            self.fail("Featured products section is not visible on the page")

        # Check subscribe form
        try:
            self.wait.until(EC.visibility_of_element_located(
                (By.NAME, "email")))
            self.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".subscribe-area-3 button.button")))
        except:
            self.fail("Subscribe form or button is not visible on the page")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()