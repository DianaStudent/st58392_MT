import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('data:text/html;charset=utf-8,{html_data}')

    def test_ui_elements(self):
        driver = self.driver
        
        # Wait and check for the header
        try:
            header = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.TAG_NAME, 'header'))
            )
        except:
            self.fail("Header is not visible or doesn't exist")
        
        # Verify logo presence
        try:
            logo = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'logo-image'))
            )
        except:
            self.fail("Logo is not visible or doesn't exist")
        
        # Verify the visibility of the search box
        try:
            search_box = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'search-input'))
            )
        except:
            self.fail("Search input is not visible or doesn't exist")
        
        # Check for the presence of 'cart-button'
        try:
            cart_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'cart-button'))
            )
        except:
            self.fail("Cart button is not visible or doesn't exist")
        
        # Verify category links in 'primary-nav'
        try:
            primary_nav = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'primary-nav'))
            )
            category_links = primary_nav.find_elements(By.TAG_NAME, 'a')
            self.assertTrue(any('/category-a' in link.get_attribute('href') for link in category_links),
                            "Category A link not found.")
            self.assertTrue(any('/category-a-1' in link.get_attribute('href') for link in category_links),
                            "Subcategory 1 link not found.")
        except:
            self.fail("Primary navigation is not visible or doesn't exist")
        
        # Verify breadcrumb presence
        try:
            breadcrumb = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'breadcrumb'))
            )
        except:
            self.fail("Breadcrumb is not visible or doesn't exist")
        
        # Check 'Sort' dropdown presence in the 'section-category'
        try:
            sort_dropdown = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'select'))
            )
        except:
            self.fail("Sort dropdown is not visible or doesn't exist")
        
        # Verify footer
        try:
            footer = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.TAG_NAME, 'footer'))
            )
        except:
            self.fail("Footer is not visible or doesn't exist")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()