from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestUIComponents(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/3-clothes")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        
        # Verify header, footer, and navigation presence
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
            footer = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "footer")))
            navigation = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-nav")))
        except Exception as e:
            self.fail(f"Critical structural element missing: {str(e)}")
        
        # Verify input fields and buttons
        try:
            search_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "s")))
            subscribe_button = self.wait.until(EC.visibility_of_element_located((By.NAME, "submitNewsletter")))
        except Exception as e:
            self.fail(f"Input fields or buttons missing: {str(e)}")
        
        # Verify links
        try:
            contact_us_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Contact us")))
            login_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
            main_logo = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "logo")))
        except Exception as e:
            self.fail(f"Required link or clickable element missing: {str(e)}")
        
        # Verify sections
        try:
            subcategory_section = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "subcategories-list")))
            product_list = self.wait.until(EC.visibility_of_element_located((By.ID, "js-product-list")))
        except Exception as e:
            self.fail(f"Primary sections missing: {str(e)}")
        
        # Interact with elements
        try:
            search_input.click()
            search_input.send_keys("T-shirt")
        except Exception as e:
            self.fail(f"Failed to interact with element: {str(e)}")
        
        # Confirm UI reaction
        try:
            subscribe_button.click()
        except Exception as e:
            self.fail(f"Failed to trigger UI reaction: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()