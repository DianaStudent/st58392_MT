import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestEcommerceFiltering(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost/")
    
    def tearDown(self):
        self.driver.quit()
    
    def test_filter_tables(self):
        # Step 1
        tables_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Tables')]")))))
        tables_button.click()
        
        # Step 2
        self.assertEqual(1, len(self.driver.find_elements_by_css_selector(".product-card")))
    
    def test_filter_chairs(self):
        # Step 3
        chairs_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Chairs')]")))))
        chairs_button.click()
        
        # Step 4
        self.assertEqual(1, len(self.driver.find_elements_by_css_selector(".product-card")))
    
    def test_remove_filter(self):
        # Step 5
        all_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'All')]")))))
        all_button.click()
        
        # Step 6
        self.assertEqual(len(self.driver.find_elements_by_css_selector(".product-card")), 0)
    
    def test_filter_tables_and_chairs(self):
        # Step 1
        tables_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Tables')]")))))
        tables_button.click()
        
        # Step 2
        self.assertEqual(1, len(self.driver.find_elements_by_css_selector(".product-card")))
    
    def test_filter_and_remove_filters(self):
        # Step 3
        chairs_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Chairs')]")))))
        chairs_button.click()
        
        # Step 4
        self.assertEqual(1, len(self.driver.find_elements_by_css_selector(".product-card")))
    
    def test_remove_filter(self):
        # Step 5
        all_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'All')]")))))
        all_button.click()
        
        # Step 6
        self.assertEqual(len(self.driver.find_elements_by_css_selector(".product-card")), 0)
    
    def test_filter_and_remove_filters(self):
        # Step 1
        tables_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Tables')]")))))
        tables_button.click()
        
        # Step 2
        self.assertEqual(1, len(self.driver.find_elements_by_css_selector(".product-card")))
    
    def test_remove_filter_and_reset_filters(self):
        # Step 3
        chairs_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Chairs')]")))))
        chairs_button.click()
        
        # Step 4
        self.assertEqual(1, len(self.driver.find_elements_by_css_selector(".product-card")))
    
    def test_remove_filter_and_reset_filters(self):
        # Step 5
        all_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'All')]")))))
        all_button.click()
        
        # Step 6
        self.assertEqual(len(self.driver.find_elements_by_css_selector(".product-card")), 0)
    
    def test_reset_filters(self):
        # Step 7
        home_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Home')]")))))
        homebutton.click()
        
        # Step 8
        self.assertEqual(len(self.driver.find_elements_by_css_selector(".product-card")), 0)
    
if __name__ == '__main__':
    unittest.main()