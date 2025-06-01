from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestEcommerceSite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_homepage(self):
        self.driver.get("http://localhost:3000")
        
        # Wait for elements to be present on the page
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1")))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='add-to-bag']")))

        # Check that required elements exist and are visible
        self.assertEqual(self.driver.find_elements(By.TAG_NAME, 'h1').__len__(), 2)
        self.assertTrue(self.driver.find_element(By.TAG_NAME, 'form').is_displayed())
        self.assertTrue(self.driver.find_element(By.XPATH, "//button[@class='add-to-bag']").is_enabled())

    def test_category_a(self):
        self.driver.get("http://localhost:3000/category-a")
        
        # Wait for elements to be present on the page
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1")))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='add-to-bag']")))

        # Check that required elements exist and are visible
        self.assertEqual(self.driver.find_elements(By.TAG_NAME, 'h1').__len__(), 2)
        self.assertTrue(self.driver.find_element(By.TAG_NAME, 'form').is_displayed())
        self.assertTrue(self.driver.find_element(By.XPATH, "//button[@class='add-to-bag']").is_enabled())

    def test_category_a_1(self):
        self.driver.get("http://localhost:3000/category-a-1")
        
        # Wait for elements to be present on the page
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1")))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='add-to-bag']")))

        # Check that required elements exist and are visible
        self.assertEqual(self.driver.find_elements(By.TAG_NAME, 'h1').__len__(), 2)
        self.assertTrue(self.driver.find_element(By.TAG_NAME, 'form').is_displayed())
        self.assertTrue(self.driver.find_element(By.XPATH, "//button[@class='add-to-bag']").is_enabled())

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()