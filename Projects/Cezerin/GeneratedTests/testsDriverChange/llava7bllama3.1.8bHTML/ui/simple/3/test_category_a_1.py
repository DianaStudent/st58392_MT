from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestWebsite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    def tearDown(self):
        self.driver.quit()

    def test_main_ui_components(self):
        self.driver.get("http://your-website-url.com")  # Replace with your website URL
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#header")))
        
        # Checking that the header is visible
        header = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#header")))
        self.assertTrue(header.is_displayed())
        
        # Checking buttons
        button_addtocart_text = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@class='checkout-button']"))).text
        self.assertIsNotNone(button_addtocart_text)
        self.assertEqual(button_addtocart_text, "Add to cart")
        
        # Checking links
        link_category_a = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/home/category_a/category_a_1']"))).text
        self.assertIsNotNone(link_category_a)
        self.assertEqual(link_category_a, "Category A 1")
        
        # Checking form fields
        search_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search product...']")))
        self.assertIsNotNone(search_input)
        
        # Checking other elements...
        home_slider_image_path = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='home-slider-image']/img"))).get_attribute('src')
        self.assertIsNotNone(home_slider_image_path)

if __name__ == '__main__':
    unittest.main()