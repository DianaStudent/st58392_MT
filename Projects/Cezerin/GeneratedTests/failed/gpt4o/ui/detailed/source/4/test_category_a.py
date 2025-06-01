from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class CategoryAPageTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        
        # Check header is visible
        header = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        self.assertIsNotNone(header)
        
        # Check logo is visible
        logo = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'logo-image')))
        self.assertIsNotNone(logo)
        
        # Check navbar is visible
        navbar = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'primary-nav')))
        self.assertIsNotNone(navbar)
        
        # Check search box is visible
        search_box = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-box')))
        self.assertIsNotNone(search_box)
        
        # Check cart button is visible
        cart_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'cart-button')))
        self.assertIsNotNone(cart_button)
        
        # Check category title is visible
        category_title = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'category-title')))
        self.assertIsNotNone(category_title)
        
        # Check sort dropdown is visible
        sort_dropdown = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'sort')))
        self.assertIsNotNone(sort_dropdown)
        
        # Check product list is visible
        products = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'products')))
        self.assertIsNotNone(products)
        
        # Check footer is visible
        footer = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
        self.assertIsNotNone(footer)
        
        # Interact with sort dropdown
        sort_select = sort_dropdown.find_element(By.TAG_NAME, 'select')
        sort_select.click()
        
        # Confirm UI reacts visually (select "Newest" option)
        newest_option = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//option[@value='-date_created']")))
        newest_option.click()
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()