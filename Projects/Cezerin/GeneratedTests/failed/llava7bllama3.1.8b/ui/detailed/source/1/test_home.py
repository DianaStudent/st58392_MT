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
        # Wait for header to be visible
        header = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//header"))
        )

        # Check main UI components are present and visible
        self.assertTrue(header.is_displayed())

        # Search bar
        search_bar = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='']"))
        )
        self.assertTrue(search_bar.is_displayed())

        # Product grid
        product_grid = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='product-grid']"))
        )
        self.assertTrue(product_grid.is_displayed())

        # Click on a button to interact with the UI
        add_to_cart_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'])[1]"))
        )
        add_to_cart_button.click()

        # Check if the product page loads correctly
        product_page_title = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//h1"))
        )
        self.assertTrue(product_page_title.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()