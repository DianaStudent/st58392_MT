from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

class TestArtPageUI(unittest.TestCase):
    
    def setUp(self):
        # Setup ChromeDriver with WebDriver Manager
        self.driver: WebDriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://localhost:8080/en/9-art')
    
    def test_ui_elements(self):
        driver = self.driver

        try:
            # Check navigation header
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "header")))
            nav_home = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/']")))
            nav_clothes = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']")))
            nav_accessories = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/6-accessories']")))
            nav_art = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']")))

            # Check for login form
            login_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art']")))

            # Interaction: Click on login link
            login_button.click()
            
            # Verify UI update - check the URL contains 'login'
            WebDriverWait(driver, 20).until(EC.url_contains('login'))

            # Check for presence of the products section
            products_section = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "products")))

            # Assume interactive buttons exist
            buttons = driver.find_elements(By.CLASS_NAME, "wishlist-button-add")
            if not buttons:
                self.fail("No interactive buttons found on the page.")

        except Exception as e:
            self.fail(f"Test failed due to exception: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()