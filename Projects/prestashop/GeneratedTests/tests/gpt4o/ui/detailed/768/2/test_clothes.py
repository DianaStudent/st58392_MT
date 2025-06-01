from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class ClothesPageTest(unittest.TestCase):
    
    def setUp(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("http://localhost:8080/en/3-clothes")

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements_presence(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Header
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
            self.assertIsNotNone(header)

            # Footer
            footer = driver.find_element(By.ID, "footer")
            self.assertTrue(footer.is_displayed())
            
            # Navigation links
            nav_links = [
                "http://localhost:8080/en/3-clothes",
                "http://localhost:8080/en/6-accessories",
                "http://localhost:8080/en/9-art"
            ]
            for link in nav_links:
                elem = driver.find_element(By.XPATH, f'//a[@href="{link}"]')
                self.assertTrue(elem.is_displayed())

            # Login and Register
            login_link = driver.find_element(By.XPATH, '//a[@href="http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F3-clothes"]')
            register_link = driver.find_element(By.XPATH, '//a[@href="http://localhost:8080/en/registration"]')
            self.assertTrue(login_link.is_displayed())
            self.assertTrue(register_link.is_displayed())
            
            # Search input field
            search_input = driver.find_element(By.XPATH, '//input[@aria-label="Search"]')
            self.assertTrue(search_input.is_displayed())

            # Subscription input field
            email_input = driver.find_element(By.XPATH, '//input[@name="email"]')
            self.assertTrue(email_input.is_displayed())

            # Subscribe button
            subscribe_button = driver.find_element(By.XPATH, '//input[@value="Subscribe"]')
            self.assertTrue(subscribe_button.is_displayed())

            # Category Section
            category_section = driver.find_element(By.ID, "js-product-list")
            self.assertTrue(category_section.is_displayed())

            # Interactions and visual confirmation
            cart_button = driver.find_element(By.CSS_SELECTOR, '.header i.shopping-cart')
            cart_button.click()
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'inactive')))
        
        except Exception as e:
            self.fail(f"UI test failed due to missing elements: {str(e)}")

if __name__ == "__main__":
    unittest.main()