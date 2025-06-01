from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestWebsite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_main_ui_components(self):
        # Navigate to the home page
        self.driver.get("http://localhost:8080/en/")

        # Check that the main UI components are present and visible
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//h1"))
        )
        
        # Check headers
        headers = ["Clothes", "Accessories", "Art"]
        for header in headers:
            self.assertIsNotNone(self.driver.find_element(By.LINK_TEXT, header))
        
        # Check links
        link_text = ["3-clothes", "6-accessories", "9-art"]
        for text in link_text:
            self.assertIsNotNone(self.driver.find_element(By.LINK_TEXT, text))
        
        # Check buttons
        self.assertIsNotNone(self.driver.find_element(By.XPATH, "//button[@id='login-button']"))
        self.assertIsNotNone(self.driver.find_element(By.XPATH, "//a[@class='btn btn-primary']"))

    def test_clothes_link(self):
        # Navigate to the clothes page
        self.driver.get("http://localhost:8080/en/3-clothes")

        # Check that the main UI components are present and visible
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//h1"))
        )

    def test_accessories_link(self):
        # Navigate to the accessories page
        self.driver.get("http://localhost:8080/en/6-accessories")

        # Check that the main UI components are present and visible
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//h1"))
        )

    def test_art_link(self):
        # Navigate to the art page
        self.driver.get("http://localhost:8080/en/9-art")

        # Check that the main UI components are present and visible
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//h1"))
        )

    def test_login_link(self):
        # Navigate to the login page
        self.driver.get("http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art")

        # Check that the main UI components are present and visible
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//h1"))
        )

    def test_register_link(self):
        # Navigate to the register page
        self.driver.get("http://localhost:8080/en/registration")

        # Check that the main UI components are present and visible
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//h1"))
        )

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()