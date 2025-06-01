import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIComponents(unittest.TestCase):

    def setUp(self):
        # Set up the Chrome WebDriver using webdriver-manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def test_ui_components(self):
        driver = self.driver

        # Wait for header to be visible
        header = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "header-area"))
        )
        self.assertIsNotNone(header, "Header not found or not visible")

        # Wait for footer to be visible
        footer = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "footer-area"))
        )
        self.assertIsNotNone(footer, "Footer not found or not visible")

        # Check presence and visibility of navigation links
        nav_links = ['Home', 'Tables', 'Chairs']
        for link_text in nav_links:
            link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, link_text))
            )
            self.assertIsNotNone(link, f"Navigation link '{link_text}' not found or not visible")

        # Check for the Accept Cookies button
        accept_cookies_btn = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, 'rcc-confirm-button'))
        )
        self.assertIsNotNone(accept_cookies_btn, "Accept Cookies button not found or not visible")
        
        # Interact with the Accept Cookies button
        accept_cookies_btn.click()

        # Check for presence and visibility of form input fields and button
        email_input = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.subscribe-form-3 input[type="email"]'))
        )
        self.assertIsNotNone(email_input, "Email input field not found or not visible")
        
        subscribe_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.subscribe-form-3 button'))
        )
        self.assertIsNotNone(subscribe_button, "Subscribe button not found or not visible")
        
        # Check and interact with product section
        product_section = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'product-area'))
        )
        self.assertIsNotNone(product_section, "Product section not found or not visible")
        
        product_buttons = driver.find_elements(By.CSS_SELECTOR, '.product-action-2 button')
        self.assertGreater(len(product_buttons), 0, "No product action buttons found")
        for button in product_buttons:
            self.assertTrue(button.is_displayed(), "Product action button is not visible")
        
        # Click a 'Add to cart' button as a visible UI interaction
        add_to_cart_button = product_buttons[0]
        add_to_cart_button.click()

    def tearDown(self):
        # Close the browser session
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()