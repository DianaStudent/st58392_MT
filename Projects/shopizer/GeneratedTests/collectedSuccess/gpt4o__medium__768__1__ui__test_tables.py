import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check for navigation links
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            tables_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            chairs_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
        except:
            self.fail("Navigation links are not visible")

        # Check for header
        try:
            header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-area")))
        except:
            self.fail("Header is not visible")
        
        # Check for buttons
        try:
            accept_cookies_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
        except:
            self.fail("Accept Cookies button is not visible or clickable")

        # Check UI updates visually when clicking a button
        try:
            cart_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "icon-cart")))
            cart_button.click()
            no_items_text = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'No items added to cart')]")))
        except:
            self.fail("Cart button or 'No items added to cart' text is not visible or clickable")

        # Verify that interactive elements do not cause errors in the UI
        try:
            subscribe_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "button")))
            subscribe_button.click()
        except:
            self.fail("Subscribe button is not visible or causes errors")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()