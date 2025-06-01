import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShopizerUITests(unittest.TestCase):
    
    def setUp(self):
        # Initialize the Chrome driver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
    
    def tearDown(self):
        # Close the browser window
        self.driver.quit()

    def test_ui_elements_present_and_interactive(self):
        driver = self.driver

        # Elements to check
        elements = {
            "home_link": (By.LINK_TEXT, "Home"),
            "tables_link": (By.LINK_TEXT, "Tables"),
            "chairs_link": (By.LINK_TEXT, "Chairs"),
            "login_link": (By.LINK_TEXT, "Login"),
            "register_link": (By.LINK_TEXT, "Register"),
            "accept_cookies_button": (By.ID, "rcc-confirm-button"),
            "shop_now_button": (By.XPATH, "//a[text()='Shop Now']"),
            "email_input": (By.XPATH, "//input[@type='email']"),
            "subscribe_button": (By.XPATH, "//button[text()='Subscribe']")
        }
        
        # Check that elements exist and are visible
        for element_name, locator in elements.items():
            try:
                WebDriverWait(driver, 20).until(EC.visibility_of_element_located(locator))
            except Exception as e:
                self.fail(f"Element '{element_name}' not found or not visible: {str(e)}")

        # Interact with the accept cookies button
        accept_cookies_button = driver.find_element(*elements["accept_cookies_button"])
        accept_cookies_button.click()

        # Interact with the 'Shop Now' button
        shop_now_button = driver.find_element(*elements["shop_now_button"])
        shop_now_button.click()

        # Verify the page updates without error
        try:
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "featured-products")))
        except Exception as e:
            self.fail(f"UI did not update as expected after clicking 'Shop Now': {str(e)}")

if __name__ == "__main__":
    unittest.main()