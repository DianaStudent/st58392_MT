import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIProcess(unittest.TestCase):

    def setUp(self):
        # Setup Chrome driver using webdriver-manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://localhost:8080/en/3-clothes')

    def test_ui_elements(self):
        driver = self.driver

        # Define elements to check
        nav_links = ['http://localhost:8080/en/3-clothes', 
                     'http://localhost:8080/en/6-accessories', 
                     'http://localhost:8080/en/9-art']
        
        # 1. Confirm presence of main UI components

        # Check navigation links
        for link in nav_links:
            try:
                element = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, f"//a[@href='{link}']"))
                )
                self.assertTrue(element.is_displayed())
            except:
                self.fail(f"Navigation link {link} is not present or not visible.")

        # Check form fields and buttons

        # Search input
        try:
            search_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='text'][name='s']"))
            )
            self.assertTrue(search_input.is_displayed())
        except:
            self.fail("Search input is not present or not visible.")

        # Sign in link
        try:
            sign_in_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Sign in"))
            )
            self.assertTrue(sign_in_link.is_displayed())
        except:
            self.fail("Sign in link is not present or not visible.")

        # Cart button
        try:
            cart_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".shopping-cart"))
            )
            self.assertTrue(cart_button.is_displayed())
        except:
            self.fail("Cart button is not present or not visible.")

        # 2. Interact with an element - click the sign in link and verify navigation
        try:
            sign_in_link.click()
            WebDriverWait(driver, 20).until(
                EC.url_contains('login')
            )
            self.assertIn("login", driver.current_url)
        except:
            self.fail("Navigation to login page failed or took too long.")

        # 3. Check no errors in UI
        try:
            # Ensure no errors are shown in the page
            error_elements = driver.find_elements(By.CLASS_NAME, "error")
            self.assertEqual(len(error_elements), 0)
        except:
            self.fail("UI errors are present on the page.")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()