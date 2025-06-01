from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestCategoryA1Page(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a-1")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check header logo
        logo = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".logo-image.active > img")))
        self.assertTrue(logo.is_displayed(), "Logo is not visible")

        # Check primary navigation links
        nav_category_a = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Category A")))
        nav_category_b = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Category B")))
        nav_category_c = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Category C")))
        self.assertTrue(nav_category_a.is_displayed(), "Category A link is not visible")
        self.assertTrue(nav_category_b.is_displayed(), "Category B link is not visible")
        self.assertTrue(nav_category_c.is_displayed(), "Category C link is not visible")

        # Check breadcrumb
        breadcrumb = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".breadcrumb")))
        self.assertTrue(breadcrumb.is_displayed(), "Breadcrumb is not visible")

        # Check category title
        category_title = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".category-title")))
        self.assertTrue(category_title.is_displayed(), "Category title is not visible")
        self.assertEqual(category_title.text, "Subcategory 1", "Category title text does not match")

        # Check search input
        search_input = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-input")))
        self.assertTrue(search_input.is_displayed(), "Search input is not visible")

        # Check sort dropdown
        sort_dropdown = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".sort select")))
        self.assertTrue(sort_dropdown.is_displayed(), "Sort dropdown is not visible")

        # Check footer
        footer = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "footer")))
        self.assertTrue(footer.is_displayed(), "Footer is not visible")

        # Interact with search input
        search_input.send_keys("test")
        self.assertEqual(search_input.get_attribute('value'), "test", "Search input did not accept typing")

        # Check shopping cart button
        cart_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart-button .icon")))
        self.assertTrue(cart_button.is_displayed(), "Cart button is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()