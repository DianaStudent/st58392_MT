import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException

class TestAccessoriesPage(unittest.TestCase):

    def setUp(self):
        # Initialize ChromeDriver using webdriver-manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/6-accessories")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_ui_elements(self):
        try:
            # Check for main UI components
            self.wait.until(EC.visibility_of_element_located((By.ID, 'header')))
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'top-menu')))
            self.wait.until(EC.visibility_of_element_located((By.ID, 'footer')))
        
            # Check for navigation links
            nav_links = [
                (By.LINK_TEXT, 'Home'),
                (By.LINK_TEXT, 'Clothes'),
                (By.LINK_TEXT, 'Accessories'),
                (By.LINK_TEXT, 'Art')
            ]
            for link in nav_links:
                self.wait.until(EC.visibility_of_element_located(link))

            # Check for form fields and buttons
            self.wait.until(EC.visibility_of_element_located((By.NAME, 's')))
            self.wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@type="submit" and @value="Subscribe"]')))
        
            # Interact with an element
            search_box = self.driver.find_element(By.NAME, 's')
            search_box.send_keys('Mug')
            submit_search = self.driver.find_element(By.XPATH, '//i[@class="material-icons search"]')
            submit_search.click()

            # Check if the page updated visually
            self.wait.until(EC.visibility_of_element_located((By.ID, 'js-product-list')))

        except TimeoutException as e:
            self.fail(f'Test failed due to missing element: {str(e)}')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()