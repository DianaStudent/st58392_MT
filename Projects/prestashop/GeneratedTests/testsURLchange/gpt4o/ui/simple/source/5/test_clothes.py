import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestClothesPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/3-clothes")
        self.driver.maximize_window()

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        try:
            # Check header is present
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
            self.assertTrue(header.is_displayed(), "Header is not visible.")
            
            # Check if the 'sign in' link is present
            sign_in_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
            self.assertTrue(sign_in_link.is_displayed(), "Sign in link is not visible.")
            
            # Check if the language dropdown is present
            language_dropdown = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "language-selector")))
            self.assertTrue(language_dropdown.is_displayed(), "Language dropdown is not visible.")
            
            # Check main category section
            main_category = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "block-category")))
            self.assertTrue(main_category.is_displayed(), "Main category section is not visible.")
            
            # Check for products
            products_section = wait.until(EC.visibility_of_element_located((By.ID, "products")))
            self.assertTrue(products_section.is_displayed(), "Products section is not visible.")
            
            # Check for filters
            filters_section = wait.until(EC.visibility_of_element_located((By.ID, "search_filters")))
            self.assertTrue(filters_section.is_displayed(), "Filters section is not visible.")
            
            # Check footer is present
            footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
            self.assertTrue(footer.is_displayed(), "Footer is not visible.")
            
        except Exception as e:
            self.fail(f"Test failed with exception: {e}")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()