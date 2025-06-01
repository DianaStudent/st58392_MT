from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check visibility of header and footer
        header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header-area')))
        self.assertTrue(header.is_displayed(), "Header is not visible")

        footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'footer-area')))
        self.assertTrue(footer.is_displayed(), "Footer is not visible")
        
        # Check navigation links
        nav_links = driver.find_elements(By.CSS_SELECTOR, 'ul > li > a')
        self.assertTrue(len(nav_links) > 0, "Navigation links are missing")
        for link in nav_links:
            self.assertTrue(link.is_displayed(), f"Navigation link {link.text} is not visible")

        # Check presence of the Accept cookies button and interact with it
        accept_cookies_button = wait.until(EC.visibility_of_element_located((By.ID, 'rcc-confirm-button')))
        self.assertTrue(accept_cookies_button.is_displayed(), "Accept cookies button is not visible")
        accept_cookies_button.click()

        # Check the presence of login and register links
        login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Login')))
        self.assertTrue(login_link.is_displayed(), "Login link is not visible")

        register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Register')))
        self.assertTrue(register_link.is_displayed(), "Register link is not visible")

        # Check presence and visibility of product items
        products = driver.find_elements(By.CLASS_NAME, 'product-wrap')
        self.assertTrue(len(products) > 0, "Product elements are missing")
        for product in products:
            self.assertTrue(product.is_displayed(), "A product element is not visible")
            # Interact with Add to Cart buttons
            add_to_cart_buttons = product.find_elements(By.CSS_SELECTOR, '.pro-cart > button')
            for button in add_to_cart_buttons:
                self.assertTrue(button.is_displayed(), "Add to cart button is not visible")
                button.click()  # Interact with button

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()