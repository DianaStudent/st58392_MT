from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CategoryPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.wait = WebDriverWait(self.driver, 20)

    def test_key_ui_elements(self):
        driver = self.driver

        # Check header visibility
        header = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        self.assertTrue(header.is_displayed(), "Header is not visible")

        # Check footer visibility
        footer = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
        self.assertTrue(footer.is_displayed(), "Footer is not visible")

        # Check navigation visibility
        primary_nav = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'primary-nav')))
        self.assertTrue(primary_nav.is_displayed(), "Primary navigation is not visible")

        # Check search box visibility
        search_box = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-input')))
        self.assertTrue(search_box.is_displayed(), "Search box is not visible")

        # Check category title visibility
        category_title = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'category-title')))
        self.assertTrue(category_title.is_displayed(), "Category title is not visible")

        # Check sidebar filter button visibility
        sidebar_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Filter products']")))
        self.assertTrue(sidebar_button.is_displayed(), "Filter products button is not visible")

        # Interaction: Check product link clickability
        product_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Product A')))
        product_link.click()

        # Assert product page is loaded by checking URL
        self.assertEqual(driver.current_url, "http://localhost:3000/category-a/product-a", "Failed to navigate to Product A page")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()