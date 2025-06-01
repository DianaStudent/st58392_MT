import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("file:///path_to_local_file/index.html")  # Point to local HTML file path
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait
        
        # Check Header
        header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        self.assertTrue(header.is_displayed(), "Header is not visible")

        # Check Footer
        footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
        self.assertTrue(footer.is_displayed(), "Footer is not visible")

        # Check Navigation for Category A
        category_a_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Category A')))
        self.assertTrue(category_a_link.is_displayed(), "Category A link is not visible")

        # Interact with Navigation
        category_a_link.click()

        # Check Subcategory
        subcategory_1_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Subcategory 1')))
        self.assertTrue(subcategory_1_link.is_displayed(), "Subcategory 1 link is not visible")

        # Interact with Subcategory
        subcategory_1_link.click()

        # Check for Input field and button in search box
        search_box_input = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-input')))
        self.assertTrue(search_box_input.is_displayed(), "Search input field is not visible")

        search_icon = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-icon-search')))
        self.assertTrue(search_icon.is_displayed(), "Search icon is not visible")

        # Click the search icon
        search_icon.click()

        # Check Main UI components
        elements = {
            "Logo": (By.CLASS_NAME, 'logo-image'),
            "Cart Button": (By.CLASS_NAME, 'cart-button'),
        }
        
        for element_name, locator in elements.items():
            try:
                element = wait.until(EC.visibility_of_element_located(locator))
                self.assertTrue(element.is_displayed(), f"{element_name} is not visible")
            except Exception as e:
                self.fail(f"{element_name} is missing: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()