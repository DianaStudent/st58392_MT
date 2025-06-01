from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestWebsiteUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://localhost/')
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_visibility(self):
        driver = self.driver
        
        # Verify header is visible
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-area")))

        # Verify navigation links are present and visible
        self.verify_element_visible(By.LINK_TEXT, "Home")
        self.verify_element_visible(By.LINK_TEXT, "Tables")
        self.verify_element_visible(By.LINK_TEXT, "Chairs")

        # Verify search field is present and visible
        # Assuming there's a search field which is not visible in HTML structure provided
        # self.verify_element_visible(By.ID, "search-input-field-id")

        # Verify the 'Accept cookies' button is present and clickable
        accept_cookies_btn = self.verify_element_clickable(By.ID, "rcc-confirm-button")
        accept_cookies_btn.click()
        
        # Verify footer is visible
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer-area")))
        
        # Verify cart button is visible
        self.verify_element_visible(By.CLASS_NAME, "icon-cart")
        
        # Verify login and register links in account dropdown
        self.verify_element_visible(By.LINK_TEXT, "Login")
        self.verify_element_visible(By.LINK_TEXT, "Register")

        # Verify product elements are visible
        self.verify_element_visible(By.XPATH, "//h3/a[contains(text(), 'Olive Table')]")
        self.verify_element_visible(By.XPATH, "//h3/a[contains(text(), 'Chair')]")
        self.verify_element_visible(By.XPATH, "//h3/a[contains(text(), 'Chair Beige')]")
        self.verify_element_visible(By.XPATH, "//h3/a[contains(text(), 'Genuine Chair')]")
        
    def verify_element_visible(self, by, value):
        try:
            element = self.wait.until(EC.visibility_of_element_located((by, value)))
            return element
        except Exception as e:
            self.fail(f"Element not found or not visible: {value}")

    def verify_element_clickable(self, by, value):
        try:
            element = self.wait.until(EC.element_to_be_clickable((by, value)))
            return element
        except Exception as e:
            self.fail(f"Element not clickable: {value}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()