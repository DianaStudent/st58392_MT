from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIElements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/9-art")
    
    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Check header visibility
        header = wait.until(EC.visibility_of_element_located((By.ID, "header")), "Header is not visible")
        
        # Verify navigation elements
        home_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/']")), "Home link is missing")
        clothes_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/3-clothes']")), "Clothes link is missing")
        accessories_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/6-accessories']")), "Accessories link is missing")
        art_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/9-art']")), "Art link is missing")
        
        # Check for the presence and visibility of the login and register links
        login_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art']")), "Login link is missing")
        register_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/registration']")), "Register link is missing")

        # Verify form fields and buttons
        search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='s']")), "Search input field is missing")
        subscribe_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='submitNewsletter']")), "Subscribe button is missing")
        
        # Check footer visibility
        footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")), "Footer is not visible")
        
        # Interact with UI elements to confirm they react as expected
        login_link.click()
        wait.until(EC.url_contains("login"), "Failed to navigate to login page")

        # Check if no required UI element is missing
        if not (header and home_link and clothes_link and accessories_link and art_link and login_link and register_link and subscribe_button and footer):
            self.fail("Some UI elements are missing")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()