from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):

    def setUp(self):
        # Setup webdriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://example.com")  # Replace this with the actual URL
        self.driver.maximize_window()

    def test_ui_elements(self):
        driver = self.driver
        
        # Verify presence of header
        header = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "header"))
        )
        self.assertTrue(header.is_displayed(), "Header is not visible")

        # Verify presence of navigation link (Category A)
        category_a_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/category-a']"))
        )
        self.assertTrue(category_a_link.is_displayed(), "Category A link is not visible")

        # Verify presence of search input field
        search_input = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input.search-input"))
        )
        self.assertTrue(search_input.is_displayed(), "Search input field is not visible")
        
        # Verify presence of sort select dropdown
        sort_dropdown = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//select"))
        )
        self.assertTrue(sort_dropdown.is_displayed(), "Sort select dropdown is not visible")
        
        # Click on Category A link and verify UI update to show Subcategory 1
        category_a_link.click()
        subcategory_1_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/category-a-1']"))
        )
        self.assertTrue(subcategory_1_link.is_displayed(), "Subcategory 1 link did not appear after clicking Category A link")
        
        # Click on Subcategory 1 link
        subcategory_1_link.click()
        
        # Verify presence of empty cart text
        cart_text = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Your cart is empty')]"))
        )
        self.assertTrue(cart_text.is_displayed(), "Cart text is not visible after interaction")

    def tearDown(self):
        # Teardown method
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()