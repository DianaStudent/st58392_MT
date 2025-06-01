from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UITest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        
        # Wait and check for main page structural elements
        header = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header.header-area")))
        self.assertIsNotNone(header, "Header is missing")
        
        footer = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer.footer-area")))
        self.assertIsNotNone(footer, "Footer is missing")

        # Check navigation links
        home_link = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/']")))
        tables_link = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/category/tables']")))
        chairs_link = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/category/chairs']")))
        self.assertIsNotNone(home_link, "Home link is missing")
        self.assertIsNotNone(tables_link, "Tables link is missing")
        self.assertIsNotNone(chairs_link, "Chairs link is missing")

        # Interact with UI elements (e.g., click a button)
        try:
            accept_cookies_button = self.wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
        except:
            self.fail("Accept cookies button not found or not clickable")

        # Check input fields
        email_input = driver.find_elements(By.CSS_SELECTOR, "input[name='email']")
        if len(email_input) == 0 or not email_input[0].is_displayed():
            self.fail("Email input field is missing or not visible")

        # Check buttons
        subscribe_button = driver.find_elements(By.CSS_SELECTOR, "button.button")
        if len(subscribe_button) == 0 or not subscribe_button[0].is_displayed():
            self.fail("Subscribe button is missing or not visible")

        # Check visible elements in product section
        product_images = driver.find_elements(By.CSS_SELECTOR, ".product-img img")
        product_buttons = driver.find_elements(By.CSS_SELECTOR, "button[title='Add to cart']")
        self.assertTrue(all(img.is_displayed() for img in product_images), "Some product images are missing or not visible")
        self.assertTrue(all(btn.is_displayed() for btn in product_buttons), "Some product buttons are missing or not visible")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()