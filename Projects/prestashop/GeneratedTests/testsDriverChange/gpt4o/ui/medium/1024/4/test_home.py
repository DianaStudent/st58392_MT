import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class TestDemoPage(unittest.TestCase):
    
    def setUp(self):
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_key_ui_elements(self):
        # Check for the presence of navigation links
        try:
            home_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            clothes_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
            accessories_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories")))
            art_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Art")))
        except Exception as e:
            self.fail(f"Navigation link not found or not visible: {e}")

        # Check for the presence of buttons and banners
        try:
            sign_in_button = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
            banner_image = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@alt='sample-1']")))
        except Exception as e:
            self.fail(f"Button or banner not found or not visible: {e}")

        # Check for the presence of form fields
        try:
            search_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "s")))
        except Exception as e:
            self.fail(f"Form field not found or not visible: {e}")

        # Interact with the search input and verify interaction
        try:
            search_input.send_keys("shirt")
            search_input.submit()
            self.wait.until(EC.url_contains("search"))
        except Exception as e:
            self.fail(f"Interaction failed or caused errors: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()