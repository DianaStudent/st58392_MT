import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):
    
    def setUp(self):
        # Setup Chrome driver
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:3000/category-a-1")

    def test_ui_elements_presence(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Ensure header is visible
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
            self.assertTrue(header.is_displayed(), "Header is not visible")
            
            # Check visibility of logo
            logo = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "logo-image")))
            self.assertTrue(logo.is_displayed(), "Logo is not visible")

            # Check presence and visibility of search bar
            search_input = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-input")))
            self.assertTrue(search_input.is_displayed(), "Search input is not visible")

            # Check presence and visibility of breadcrumb
            breadcrumb = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "breadcrumb")))
            self.assertTrue(breadcrumb.is_displayed(), "Breadcrumb is not visible")

            # Verify footer visibility
            footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "footer")))
            self.assertTrue(footer.is_displayed(), "Footer is not visible")

            # Interact with filter button
            filter_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "button")))
            filter_button.click()

            # Confirm if filter interaction reacts visually
            filter_options = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "price-filter")))
            self.assertTrue(filter_options.is_displayed(), "Filter options did not appear on click")

            # Confirm category navigation links are present
            category_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Category A")))
            self.assertTrue(category_link.is_displayed(), "Category link 'Category A' is not visible")

            subcategory_1_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Subcategory 1")))
            self.assertTrue(subcategory_1_link.is_displayed(), "Subcategory link 'Subcategory 1' is not visible")
        
        except Exception as e:
            self.fail(f"A required UI element is missing or not visible: {str(e)}")

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()