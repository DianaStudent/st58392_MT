import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestDefaultStoreUI(unittest.TestCase):
    
    def setUp(self):
        # Set up the ChromeDriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)
        
    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait
        
        # Check header is visible
        header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header.header-area")))
        self.assertIsNotNone(header, "Header is not visible")
        
        # Check navigation links are visible
        navigation_links = [
            (By.LINK_TEXT, "Home"),
            (By.LINK_TEXT, "Tables"),
            (By.LINK_TEXT, "Chairs"),
            (By.LINK_TEXT, "Login"),
            (By.LINK_TEXT, "Register")
        ]
        for link_text, selector in navigation_links:
            nav_link = wait.until(EC.visibility_of_element_located((link_text, selector)))
            self.assertIsNotNone(nav_link, f"Navigation link '{selector}' is not visible")
        
        # Check footer is visible
        footer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer.footer-area")))
        self.assertIsNotNone(footer, "Footer is not visible")
        
        # Check presence and visibility of the newsletter subscription input field and button
        subscribe_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.email[name='email']")))
        self.assertIsNotNone(subscribe_input, "Subscribe input is not visible")
        
        subscribe_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.clear-3 button.button")))
        self.assertIsNotNone(subscribe_button, "Subscribe button is not visible")
        
        # Interact with the "Add to cart" button for the Olive Table
        olive_table_cart_button = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[@class='product-content-2']//a[text()='Olive Table']/ancestor::div[@class='product-wrap-2']//button[@title='Add to cart']")
            )
        )
        self.assertIsNotNone(olive_table_cart_button, "Olive Table 'Add to cart' button is not visible")
        olive_table_cart_button.click()
        
        # Verify shopping cart content changes visually
        cart_count = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.count-style")))
        self.assertEqual(cart_count.text, "1", "Cart count did not update after adding item")
        
        # Ensure no required UI element is missing
        required_elements = [
            header, footer, subscribe_input, subscribe_button,
            olive_table_cart_button, cart_count
        ]
        for elem in required_elements:
            if elem is None:
                self.fail("One or more required UI elements are missing.")
        
    def tearDown(self):
        # Clean up and close the browser
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main()