import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class ArtPageUITest(unittest.TestCase):
    
    def setUp(self):
        # Setup Chrome WebDriver using webdriver-manager
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/9-art")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_ui_elements_presence(self):
        # Check if navigation links and logo are present and visible
        self.assert_element_visible(By.CSS_SELECTOR, "a[href='http://localhost:8080/en/']", "Home link")
        self.assert_element_visible(By.CSS_SELECTOR, "a[href='http://localhost:8080/en/3-clothes']", "Clothes link")
        self.assert_element_visible(By.CSS_SELECTOR, "a[href='http://localhost:8080/en/6-accessories']", "Accessories link")
        self.assert_element_visible(By.CSS_SELECTOR, "a[href='http://localhost:8080/en/9-art']", "Art link")
        self.assert_element_visible(By.CSS_SELECTOR, "a[href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art']", "Login link")
        
        # Check for presence of search input
        self.assert_element_visible(By.CSS_SELECTOR, "#search_widget input[name='s']", "Search input")
        
        # Check for presence of shopping cart button
        self.assert_element_visible(By.CSS_SELECTOR, "div.header .shopping-cart", "Shopping cart icon")
        
        # Check for presence of sign in button
        self.assert_element_visible(By.CSS_SELECTOR, "a[href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art']", "Sign in button")
        
        # Interact with 'Sign in' link and verify no errors
        sign_in_link = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art']")))
        sign_in_link.click()
        self.wait.until(EC.url_contains("/en/login"))

    def assert_element_visible(self, by, locator, element_name):
        try:
            element = self.wait.until(EC.visibility_of_element_located((by, locator)))
            self.assertTrue(element.is_displayed(), f"{element_name} is not visible")
        except Exception as e:
            self.fail(f"{element_name} was not found or is not visible: {str(e)}")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()