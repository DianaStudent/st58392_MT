from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestEcommerceWebsite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_homepage_elements(self):
        # Check that the main UI components are present
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1[@class='page-title']")))
        
        # Check header title
        self.assertEqual(self.driver.find_element(By.XPATH, "//h1[@class='page-title']").text, "Ecommerce Website")

        # Check navigation links
        self.assertTrue(self.driver.find_element(By.XPATH, "//nav//a[@href='/en/3-clothes']").is_displayed())
        self.assertTrue(self.driver.find_element(By.XPATH, "//nav//a[@href='/en/6-accessories']").is_displayed())
        self.assertTrue(self.driver.find_element(By.XPATH, "//nav//a[@href='/en/9-art']").is_displayed())

    def test_clothes_page_elements(self):
        self.driver.get("http://localhost:8080/en/3-clothes")
        
        # Check header title
        self.assertEqual(self.driver.find_element(By.XPATH, "//h1[@class='page-title']").text, "Clothes")

        # Check product list
        products = self.driver.find_elements(By.XPATH, "//div[@class='product-list']//a")
        self.assertGreaterEqual(len(products), 5)

    def test_accessories_page_elements(self):
        self.driver.get("http://localhost:8080/en/6-accessories")
        
        # Check header title
        self.assertEqual(self.driver.find_element(By.XPATH, "//h1[@class='page-title']").text, "Accessories")

        # Check product list
        products = self.driver.find_elements(By.XPATH, "//div[@class='product-list']//a")
        self.assertGreaterEqual(len(products), 5)

    def test_art_page_elements(self):
        self.driver.get("http://localhost:8080/en/9-art")
        
        # Check header title
        self.assertEqual(self.driver.find_element(By.XPATH, "//h1[@class='page-title']").text, "Art")

        # Check product list
        products = self.driver.find_elements(By.XPATH, "//div[@class='product-list']//a")
        self.assertGreaterEqual(len(products), 5)

    def test_login_page_elements(self):
        self.driver.get("http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art")
        
        # Check form fields
        self.assertTrue(self.driver.find_element(By.XPATH, "//input[@name='email']").is_displayed())
        self.assertTrue(self.driver.find_element(By.XPATH, "//input[@name='password']").is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()