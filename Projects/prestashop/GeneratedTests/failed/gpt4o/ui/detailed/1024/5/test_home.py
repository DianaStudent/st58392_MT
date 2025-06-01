from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestWebsiteUI(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_presence(self):
        
        try:
            # Check header is visible
            header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
            
            # Check footer is visible
            footer = self.wait.until(EC.visibility_of_element_located((By.ID, "footer")))
            
            # Check navigation links
            clothes_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
            accessories_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories")))
            art_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Art")))
            
            # Check login link
            login_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
            
            # Check search input
            search_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "s")))
            
            # Check subscribe button
            subscribe_button = self.wait.until(EC.visibility_of_element_located((By.NAME, "submitNewsletter")))
            
            # Check Sign in button in user info
            user_info = self.wait.until(EC.visibility_of_element_located((By.ID, "_desktop_user_info")))
            sign_in_button = user_info.find_element(By.TAG_NAME, 'a')
            
            # Interaction: Click on "Clothes" link and check
            clothes_link.click()
            self.wait.until(EC.url_contains("3-clothes"))
            
        except Exception as e:
            self.fail(f"UI element missing or not visible: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()