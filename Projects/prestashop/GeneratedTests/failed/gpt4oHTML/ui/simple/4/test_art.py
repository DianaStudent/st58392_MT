from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestArtPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost:8080/en/9-art')
    
    def test_presence_of_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Check header presence
            header = wait.until(EC.visibility_of_element_located((By.ID, 'header')))
        except Exception as e:
            self.fail(f"Header not found: {e}")
        
        try:
            # Check main menu links
            home_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/']")))
            clothes_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/3-clothes']")))
            accessories_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/6-accessories']")))
            art_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/9-art']")))
        except Exception as e:
            self.fail(f"Main menu link not found: {e}")

        try:
            # Check sign in presence 
            sign_in_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art']")))
        except Exception as e:
            self.fail(f"Sign in link not found: {e}")

        try:
            # Check register presence
            register_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/registration']")))
        except Exception as e:
            self.fail(f"Register link not found: {e}")

        try:
            # Check search field presence
            search_widget = wait.until(EC.visibility_of_element_located((By.ID, 'search_widget')))
        except Exception as e:
            self.fail(f"Search widget not found: {e}")

        try:
            # Check footer presence
            footer = wait.until(EC.visibility_of_element_located((By.ID, 'footer')))
        except Exception as e:
            self.fail(f"Footer not found: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()