from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class UITestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Confirming presence of navigation links
        navigation_links = {
            "home": "http://localhost:8080/en/",
            "clothes": "http://localhost:8080/en/3-clothes",
            "accessories": "http://localhost:8080/en/6-accessories",
            "art": "http://localhost:8080/en/9-art",
            "login": "http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art",
            "register": "http://localhost:8080/en/registration"
        }
        
        for key, url in navigation_links.items():
            try:
                element = self.wait.until(
                    EC.visibility_of_element_located((By.XPATH, f"//a[@href='{url}']"))
                )
            except:
                self.fail(f"Navigation link for {key} not found")
        
        # Confirming presence of key elements
        key_elements = [
            "//div[@class='header-nav']", # header nav
            "//div[@class='header-banner']", # header banner
            "//form[@action='//localhost:8080/en/search']", # search form
            "//a[@class='banner']" # banner
        ]

        for selector in key_elements:
            try:
                element = self.wait.until(
                    EC.visibility_of_element_located((By.XPATH, selector))
                )
            except:
                self.fail(f"Key UI element {selector} not found or not visible")

        # Interact with a button
        try:
            button = self.wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "wishlist-button-add"))
            )
            button.click()

            # Verify UI updates visually (check for presence of a modal or wishlist)
            self.wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "wishlist-list"))
            )
        except:
            self.fail("Button interaction did not update UI as expected or caused errors")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()