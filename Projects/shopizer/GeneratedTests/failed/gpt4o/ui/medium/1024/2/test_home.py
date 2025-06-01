from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestShopizerUI(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        # Check for the navigation elements
        try:
            nav_home = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            nav_tables = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            nav_chairs = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
        except:
            self.fail("Navigation links are missing or not visible.")

        # Check for the banner
        try:
            banner = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".site-block-cover-content h1")))
            self.assertEqual(banner.text, "Imports from the world")
        except:
            self.fail("Banner is missing or not visible.")

        # Check for the "Shop Now" button
        try:
            shop_now_button = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Shop Now")))
        except:
            self.fail("'Shop Now' button is missing or not visible.")

        # Check for featured products section
        try:
            featured_products_title = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".section-title-5")))
            self.assertEqual(featured_products_title.text, "Featured Products")
        except:
            self.fail("Featured products section is missing or not visible.")

        # Interact with "Shop Now" button
        try:
            shop_now_button.click()
            # wait for potential page update after clicking "Shop Now", could be checking URL change here
        except:
            self.fail("Clicking 'Shop Now' caused UI issues or errors.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()