import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestDemoPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://localhost:8080/en/')
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Verify header elements
        try:
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
            self.assertTrue(header.is_displayed(), "Header is not visible")
            
            nav_bar = header.find_element(By.CLASS_NAME, "header-nav")
            self.assertTrue(nav_bar.is_displayed(), "Navigation bar is not visible")
      
        except Exception as e:
            self.fail(f"Header elements missing or not visible: {e}")
        
        # Verify main content
        try:
            main_content = wait.until(EC.visibility_of_element_located((By.ID, "content-wrapper")))
            self.assertTrue(main_content.is_displayed(), "Main content is not visible")

            # Check banner presence
            banner = main_content.find_element(By.CLASS_NAME, "banner")
            self.assertTrue(banner.is_displayed(), "Banner is not visible")
        
        except Exception as e:
            self.fail(f"Main content or banner missing or not visible: {e}")
        
        # Verify popular products section
        try:
            featured_section = main_content.find_element(By.CLASS_NAME, "featured-products")
            self.assertTrue(featured_section.is_displayed(), "Featured products section is not visible")
            
            product_items = featured_section.find_elements(By.CLASS_NAME, "product-miniature")
            self.assertGreater(len(product_items), 0, "No product items found in featured products section")
        
        except Exception as e:
            self.fail(f"Featured products section missing or not visible: {e}")
        
        # Interact with an element (example: Quick view button)
        try:
            quick_view_button = product_items[0].find_element(By.CLASS_NAME, "quick-view")
            quick_view_button.click()

            # Assuming a modal opens up
            modal = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wishlist-modal")))
            self.assertTrue(modal.is_displayed(), "Quick view modal did not appear")

        except Exception as e:
            self.fail(f"Quick view interaction failed: {e}")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()