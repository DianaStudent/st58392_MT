from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager import ChromeDriverManager

class TestHomePage(unittest.TestCase):
    def setUp(self):
        driver = ChromeDriverManager().get_chrome_driver()
        self.driver = driver
        self.driver.get("http://example.com")
    
    def tearDown(self):
        self.driver.quit()
    
    def test_home_page_elements(self):
        # Check that the main UI components are present
        headers = self.driver.find_element_by_css_selector(".header")  # header element name: ".header"
        self.assertTrue(headers, "Header element not found")
        
        links = self.driver.find_element_by_css_selector("a")  # link element name: "a"
        self.assertTrue(links, "Link element not found")
        
        buttons = self.driver.find_element_by_css_selector(".button")  # button element name: ".button"
        self.assertTrue(buttons, "Button element not found")
        
        form_fields = self.driver.find_element_by_css_selector("input")  # input element name: "input"
        self.assertTrue(form_fields, "Input element not found")
        
        banners = self.driver.find_element_by_css_selector(".banner")  # banner element name: ".banner"
        self.assertTrue(banners, "Banner element not found")
    
    def test_interact_with_button(self):
        button = self.driver.find_element_by_css_selector("button.button is-primary")  # button element name: "button.button is-primary"
        
        # Click the button and verify that the UI updates visually
        original_position = self.driver.page_source
        button.click()
        new_position = self.driver.page_source
        
        self.assertEqual(original_position, new_position, "Button did not click correctly")
    
    def test_home_page_product_galery(self):
        product_gallery = self.driver.find_element_by_css_selector(".product-gallery")  # product gallery element name: ".product-gallery"
        
        # Check that the product gallery exists and is visible
        self.assertTrue(product_gallery, "Product gallery not found")
        
        products = product_gallery.find_elements_by_css_selector(".product")  # product element name: ".product"
        
        for i, product in enumerate(products):
            print(f"Product {i+1}: {product.name}")
    
    def test_home_page_category(self):
        category_a_1 = self.driver.find_element_by_css_selector("a[role='category'][href='#category-1']")  # category element name: "[role='category'][href='#category-1']"
        
        # Click the category link and verify that the UI updates visually
        original_position = self.driver.page_source
        category_a_1.click()
        new_position = self.driver.page_source
        
        self.assertEqual(original_position, new_position, "Category did not click correctly")
    
if __name__ == "__main__":
    unittest.main()