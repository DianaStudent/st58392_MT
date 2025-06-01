from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import os
from selenium.webdriver.chrome.service import Service as ChromeService

class TestHomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/")

    def test_home_page_components(self):
        # Verify header
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h1[text()='Welcome to Max']"))
        )
        
        # Verify search bar
        search_bar = self.driver.find_element(By.XPATH, "//input[@placeholder='Search...']")
        self.assertIsNotNone(search_bar)
        
        # Verify welcome message
        welcome_message = self.driver.find_element(By.XPATH, "//p[@class='welcome-message']")
        self.assertIsNotNone(welcome_message)
        
        # Verify sign in button
        sign_in_button = self.driver.find_element(By.XPATH, "//button[text()='Sign In']")
        self.assertIsNotNone(sign_in_button)

    def tearDown(self):
        if os.path.exists("screenshots"):
            for filename in os.listdir("./screenshots"):
                os.remove(os.path.join("./screenshots", filename))
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()