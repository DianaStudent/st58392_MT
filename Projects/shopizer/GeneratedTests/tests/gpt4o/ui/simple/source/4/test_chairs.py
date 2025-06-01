import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class ShopizerUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get("http://localhost/")
        self.driver.set_window_size(1920, 1080)

    def test_ui_elements_present(self):
        driver = self.driver

        # Check for header and navigation links
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-area")))
        
        # Check presence of main menu links: Home, Tables, Chairs
        nav_links = {
            "Home": "/",
            "Tables": "/category/tables",
            "Chairs": "/category/chairs",
        }
        for link_text, link_href in nav_links.items():
            link = driver.find_element(By.XPATH, f'//a[@href="{link_href}"]')
            if not link.is_displayed():
                self.fail(f"Navigation link '{link_text}' not visible")

        # Check for Cookie Consent button
        cookie_button = self.wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
        if not cookie_button.is_displayed():
            self.fail("Cookie consent button not visible")

        # Check for account setting button
        account_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "account-setting-active")))
        if not account_button.is_displayed():
            self.fail("Account setting button not visible")

        # Check for the cart icon
        cart_icon = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "icon-cart")))
        if not cart_icon.is_displayed():
            self.fail("Cart icon not visible")

        # Check product listings for Olive Table
        olive_table = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@href="/product/olive-table"]')))
        if not olive_table.is_displayed():
            self.fail("Product 'Olive Table' not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()