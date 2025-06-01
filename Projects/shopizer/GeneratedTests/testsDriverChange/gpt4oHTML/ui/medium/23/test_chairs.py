import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost/")
    
    def test_ui_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check for main navigation links
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            tables_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            chairs_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
            login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
            register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
        except Exception as e:
            self.fail(f"Navigation links not found: {str(e)}")

        # Check for the cookie acceptance button
        try:
            cookie_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
        except Exception as e:
            self.fail(f"Cookie acceptance button not found: {str(e)}")

        # Check headers
        try:
            header_area = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-area")))
        except Exception as e:
            self.fail(f"Header area not found: {str(e)}")

        # Interact with the 'Accept' button to check UI update
        try:
            cookie_button.click()
        except Exception as e:
            self.fail(f"Failed to click on 'Accept' cookies button: {str(e)}")

        # Verify the shopping cart button
        try:
            cart_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "icon-cart")))
        except Exception as e:
            self.fail(f"Cart button not found: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()