from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestEcommerceSite(unittest.TestCase):

    def setUp(self):
        options = Options()
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def tearDown(self):
        self.driver.quit()

    # Test case for checking UI components
    def test_check_ui_components(self):
        expected_headers = ["Clothes", "Accessories", "Art"]
        expected_buttons = ["Login", "Register"]
        expected_links = ["home:http://localhost:8080/en/", 
                          "clothes:http://localhost:8080/en/3-clothes",
                          "accessories:http://localhost:8080/en/6-accessories",
                          "art:http://localhost:8080/en/9-art",
                          "login:http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art"]

        # Check main menu header
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h1")))
        self.failUnless(EC.visibility_of_element_located((By.XPATH, "//h1")).is_displayed())

        # Check sub-menu headers
        for i in expected_headers:
            self.failUnless(EC.visibility_of_element_located((By.XPATH, f"//a[text()='{i}']")).is_displayed())

        # Check buttons
        for button in expected_buttons:
            self.failUnless(EC.visibility_of_element_located((By.XPATH, f"//button[text()='{button}']")).is_displayed())

        # Check links
        for link in expected_links:
            self.failUnless(EC.visibility_of_element_located((By.XPATH, f"//a[@href='{link}']")).is_displayed())

    def test_check_elements(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//h1"))
            )
            self.failUnless(EC.visibility_of_element_located((By.XPATH, "//h1")).is_displayed())
            
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
            )
            self.failUnless(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")).is_displayed())

        except:
            self.fail("Elements not found")

if __name__ == "__main__":
    unittest.main()