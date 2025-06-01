from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class ShopizerUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost/')
        self.driver.set_window_size(1920, 1080)

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Verify header is present and visible
        header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'header.header-area')))
        self.assertTrue(header.is_displayed(), "Header is not visible")

        # Verify footer is present and visible
        footer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'footer.footer-area')))
        self.assertTrue(footer.is_displayed(), "Footer is not visible")
        
        # Verify navigation links are present and visible
        nav_links = [
            (By.LINK_TEXT, 'Home'),
            (By.LINK_TEXT, 'Tables'),
            (By.LINK_TEXT, 'Chairs'),
        ]
        for link in nav_links:
            element = wait.until(EC.visibility_of_element_located(link))
            self.assertTrue(element.is_displayed(), f"Navigation link {link} is not visible")

        # Verify login and register links
        login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Login')))
        register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Register')))

        self.assertTrue(login_link.is_displayed(), "Login link is not visible")
        self.assertTrue(register_link.is_displayed(), "Register link is not visible")

        # Check and interact with the "Accept cookies" button
        accept_cookies_btn = wait.until(EC.visibility_of_element_located((By.ID, 'rcc-confirm-button')))
        self.assertTrue(accept_cookies_btn.is_displayed(), "Accept cookies button is not visible")
        accept_cookies_btn.click()

        # Check products section
        products_text = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.shop-top-bar')))
        self.assertTrue(products_text.is_displayed(), "Products section is not visible")

        # Check visibility and interaction of "Add to cart" button for the first product
        add_to_cart_btn = wait.until(EC.visibility_of_element_located((By.XPATH, "(//button[@title='Add to cart'])[1]")))
        self.assertTrue(add_to_cart_btn.is_displayed(), "Add to cart button for the first product is not visible")
        
        # Interacting visually (not required to click to avoid complications in testing)
        # add_to_cart_btn.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()