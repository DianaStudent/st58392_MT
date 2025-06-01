from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alerts import Alert
from selenium.webdriver.common.exceptions import NoNewWindowsException
from selenium.webdriver.common.keys import Key

class TestWebpage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 20)
        
    def tearDown(self):
        self.driver.quit()

    def test_home_page(self):
        try:
            self.driver.get("https://www.example.com/")
            self.assertEqual(self.driver.title,"Home Page Title")
            
            # Add category
            category_input = self.wait.until(EC.element_located((By.XPATH, "//input[@name='category']")))
            category_input.send_keys("Category A")
            category_button = self.wait.until(EC.element_located((By.XPATH, "//button[@type='submit']")))
            self.wait.until(EC.element_located((By.XPATH, "//input[@id='product_name']")))
            product_name_input = self.wait.until(EC.element_located((By.XPATH, "//input[@name='product_name']")))
            product_name_input.send_keys("Product Name")
            
            # Add product
            product_price_input = self.wait.until(EC.element_located((By.XPATH, "//input[@id='price']")))
            product_price_input.send_keys("100.0")
            product_description_input = self.wait.until(EC.element_located((By.XPATH, "//input[@id='description']")))
            product_description_input.send_keys("Product Description")
            
            # Add category
            category_1_input = self.wait.until(EC.element_located((By.XPATH, "//input[@name='category_1']")))
            category_1_input.send_keys("Category 1")
            category_2_input = self.wait.until(EC.element_located((By.XPATH, "//input[@id='category_2']")))
            category_2_input.send_keys("Category 2")
            submit_button = self.wait.until(EC.element_located((By.XPATH, "//button[@type='submit']")))
            
            # Confirm UI reactions
            self.assertEqual(self.driver.title,"Product Listing Page Title")
            self.wait.until(EC.element_located((By.XPATH, "//h1[contains(text(),'List of Products')]")))
            product_list = self.wait.until(EC.element_located((By.XPATH, "//ul[contains(@class,'product-list')]")))
            
        except NoNewWindowsException as e:
            print("New window is not allowed")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    unittest.main()