from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestAccessoriesPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/6-accessories")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Check that the main structural elements are visible
            wait.until(EC.visibility_of_element_located((By.ID, 'header')))
            wait.until(EC.visibility_of_element_located((By.ID, 'footer')))
            
            # Check navigation links
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Home')))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Clothes')))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Accessories')))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Art')))
            
            # Check presence of search widget
            wait.until(EC.visibility_of_element_located((By.ID, 'search_widget')))
            
            # Check presence of sign in link
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Sign in')))

            # Check presence of the contact us link
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Contact us')))
            
            # Check product list section
            wait.until(EC.visibility_of_element_located((By.ID, 'products')))
        
            # Interact with a button (example: filter button if exists)
            filter_buttons = driver.find_elements(By.CLASS_NAME, 'btn')
            if filter_buttons:
                filter_buttons[0].click()
            
        except Exception as e:
            self.fail(f"Test failed due to missing element: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()