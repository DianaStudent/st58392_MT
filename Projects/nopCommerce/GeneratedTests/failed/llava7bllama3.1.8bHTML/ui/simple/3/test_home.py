from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestMaxWebsite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")

    def test_main_ui_components(self):
        # Wait for header elements to be visible
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".header")))
        
        # Check that main UI components are present
        self.assertEqual(len(self.driver.find_elements(By.CSS_SELECTOR, ".header")), 1)
        
        # Wait for buttons and links to be visible
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button")))
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a")))
        
        # Check that these elements exist and are visible
        self.assertGreater(len(self.driver.find_elements(By.CSS_SELECTOR, "button")), 0)
        self.assertGreater(len(self.driver.find_elements(By.CSS_SELECTOR, "a")), 0)
        
        # Wait for form fields to be visible
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input")))
        
        # Check that these elements exist and are visible
        self.assertGreater(len(self.driver.find_elements(By.CSS_SELECTOR, "input")), 0)

    def test_login_page_ui_components(self):
        # Click on login button
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#login"))).click()
        
        # Wait for header elements to be visible
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".header")))
        
        # Check that main UI components are present
        self.assertEqual(len(self.driver.find_elements(By.CSS_SELECTOR, ".header")), 1)
        
        # Wait for buttons and links to be visible
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button")))
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a")))
        
        # Check that these elements exist and are visible
        self.assertGreater(len(self.driver.find_elements(By.CSS_SELECTOR, "button")), 0)
        self.assertGreater(len(self.driver.find_elements(By.CSS_SELECTOR, "a")), 0)
        
        # Wait for form fields to be visible
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input")))
        
        # Check that these elements exist and are visible
        self.assertGreater(len(self.driver.find_elements(By.CSS_SELECTOR, "input")), 0)
        
        # Click on return url button to go back to main page
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#return-url"))).click()

    def test_register_page_ui_components(self):
        # Click on register link
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#register"))).click()
        
        # Wait for header elements to be visible
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".header")))
        
        # Check that main UI components are present
        self.assertEqual(len(self.driver.find_elements(By.CSS_SELECTOR, ".header")), 1)
        
        # Wait for buttons and links to be visible
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button")))
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a")))
        
        # Check that these elements exist and are visible
        self.assertGreater(len(self.driver.find_elements(By.CSS_SELECTOR, "button")), 0)
        self.assertGreater(len(self.driver.find_elements(By.CSS_SELECTOR, "a")), 0)
        
        # Wait for form fields to be visible
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input")))
        
        # Check that these elements exist and are visible
        self.assertGreater(len(self.driver.find_elements(By.CSS_SELECTOR, "input")), 0)
        
    def test_search_page_ui_components(self):
        # Click on search link
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#search"))).click()
        
        # Wait for header elements to be visible
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".header")))
        
        # Check that main UI components are present
        self.assertEqual(len(self.driver.find_elements(By.CSS_SELECTOR, ".header")), 1)
        
        # Wait for buttons and links to be visible
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button")))
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a")))
        
        # Check that these elements exist and are visible
        self.assertGreater(len(self.driver.find_elements(By.CSS_SELECTOR, "button")), 0)
        self.assertGreater(len(self.driver.find_elements(By.CSS_SELECTOR, "a")), 0)
        
        # Wait for form fields to be visible
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input")))
        
        # Check that these elements exist and are visible
        self.assertGreater(len(self.driver.find_elements(By.CSS_SELECTOR, "input")), 0)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()