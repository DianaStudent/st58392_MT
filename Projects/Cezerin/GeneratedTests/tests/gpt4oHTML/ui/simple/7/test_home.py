from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class HomePageUITest(unittest.TestCase):

    def setUp(self):
        # Setup Chrome driver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://example.com")  # Replace with the actual URL
        self.driver.maximize_window()

    def test_home_ui_components(self):
        driver = self.driver
        try:
            # Wait for and check header
            header = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.TAG_NAME, 'header'))
            )

            # Check logo presence
            logo = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'img[alt="logo"]'))
            )

            # Check main navigation
            nav = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '.primary-nav'))
            )

            # Check search box
            search_box = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '.search-box input[type="text"]'))
            )

            # Check cart button
            cart_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '.cart-button img[alt="cart"]'))
            )

            # Check category links
            category_a = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, 'Category A'))
            )

            # Click on Category A to check subcategories
            category_a.click()

            subcategory_1 = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, 'Subcategory 1'))
            )
            subcategory_2 = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, 'Subcategory 2'))
            )
            subcategory_3 = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, 'Subcategory 3'))
            )

        except Exception as e:
            self.fail(f"Failed to find a required element: {e}")

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()