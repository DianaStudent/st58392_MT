from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CategoryATest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.driver.maximize_window()
    
    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header visibility
        header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
        self.assertIsNotNone(header, "Header is not visible")

        # Check footer visibility
        footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "footer")))
        self.assertIsNotNone(footer, "Footer is not visible")

        # Check navigation menu visibility
        nav_menu = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "primary-nav")))
        self.assertIsNotNone(nav_menu, "Navigation menu is not visible")

        # Check search box visibility
        search_box = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-box")))
        self.assertIsNotNone(search_box, "Search box is not visible")

        # Check product list visibility
        products = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "products")))
        self.assertIsNotNone(products, "Product list is not visible")

        # Check category title visibility
        category_title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "category-title")))
        self.assertIsNotNone(category_title, "Category title is not visible")

        # Interact with sort dropdown
        sort_dropdown = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "select")))
        sort_dropdown.click() # Trigger dropdown
        favorite_option = wait.until(EC.visibility_of_element_located((By.XPATH, "//option[@value='stock_status,price,position']")))
        self.assertIsNotNone(favorite_option, "Favorite option is not visible in sort dropdown")
        favorite_option.click()

        # Assert the reaction to the interaction
        # Here we are assuming that selecting "Favorite" triggers some UI change
        # You should replace the comment below with actual checks for your UI change
        # self.assertTrue(condition, "UI did not react as expected")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()