from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUI(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000")

    def test_ui_elements(self):
        # Header
        header = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#header"))
        )
        self.assertTrue(header.is_displayed())

        # Navigation links
        navigation_links = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".nav-link"))
        )
        self.assertGreater(len(navigation_links), 0)

        # Product image
        product_image = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".product-image"))
        )
        self.assertTrue(product_image.is_displayed())

        # Product title and description
        product_title = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".product-title"))
        )
        self.assertTrue(product_title.is_displayed())
        product_description = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".product-description"))
        )
        self.assertTrue(product_description.is_displayed())

        # Bottom navigation
        bottom_navigation = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#bottom-navigation"))
        )
        self.assertTrue(bottom_navigation.is_displayed())

        # Interact with a button
        product_image.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()