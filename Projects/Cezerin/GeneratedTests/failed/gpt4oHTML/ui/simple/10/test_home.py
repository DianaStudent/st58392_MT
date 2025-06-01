from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestUIComponents(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost")  # Change URL to the actual page

    def tearDown(self):
        self.driver.quit()

    def test_ui_components(self):
        driver = self.driver

        try:
            # Check header
            header = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.TAG_NAME, "header"))
            )
            self.assertTrue(header.is_displayed(), "Header is not visible")
        
            # Check main category link
            category_a = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a[@href='/category-a']"))
            )
            self.assertTrue(category_a.is_displayed(), "Category A link is not visible")
            category_a.click()

            # Check subcategory link
            subcategory = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a[@href='/category-a-1']"))
            )
            self.assertTrue(subcategory.is_displayed(), "Subcategory 1 link is not visible")
            subcategory.click()

            # Check search box
            search_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "search-input"))
            )
            self.assertTrue(search_input.is_displayed(), "Search input is not visible")

            # Check cart button
            cart_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "cart-button"))
            )
            self.assertTrue(cart_button.is_displayed(), "Cart button is not visible")

        except Exception as e:
            self.fail(f"Failed with exception: {e}")

if __name__ == "__main__":
    unittest.main()