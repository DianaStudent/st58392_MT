from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCategoryAPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")

    def test_ui_elements_presence(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Check header elements
        try:
            logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a.logo-image')))
            self.assertTrue(logo.is_displayed(), "Logo is not visible")
            
            # Ensure menu links are visible
            menu_links = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'ul.nav-level-0 > li')))
            self.assertGreaterEqual(len(menu_links), 3, "Not all menu categories are present")

        except Exception as e:
            self.fail(f"Header elements are missing: {str(e)}")

        # Check search and cart are present
        try:
            search_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.search-input')))
            self.assertTrue(search_box.is_displayed(), "Search box is not visible")

            cart_icon = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span.cart-button')))
            self.assertTrue(cart_icon.is_displayed(), "Cart icon is not visible")
            
        except Exception as e:
            self.fail(f"Search and cart elements are missing: {str(e)}")

        # Check breadcrumb
        try:
            breadcrumb = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav.breadcrumb a.active')))
            self.assertTrue(breadcrumb.is_displayed(), "Breadcrumb is not visible")
        
        except Exception as e:
            self.fail(f"Breadcrumb is missing: {str(e)}")
        
        # Check sort dropdown
        try:
            sort_dropdown = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.sort select')))
            self.assertTrue(sort_dropdown.is_displayed(), "Sort dropdown is not visible")
        
        except Exception as e:
            self.fail(f"Sort dropdown is missing: {str(e)}")
        
        # Check products are listed
        try:
            products = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div.products > div.available')))
            self.assertGreaterEqual(len(products), 2, "Not all products are visible")

        except Exception as e:
            self.fail(f"Product listings are missing: {str(e)}")

        # Check footer
        try:
            footer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section.section-footer')))
            self.assertTrue(footer.is_displayed(), "Footer is not visible")
        
        except Exception as e:
            self.fail(f"Footer is missing: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()