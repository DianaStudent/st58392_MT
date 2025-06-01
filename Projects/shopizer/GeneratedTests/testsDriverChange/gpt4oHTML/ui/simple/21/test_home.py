import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService

class UITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost/')
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_components(self):
        driver = self.driver

        # Check header
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header-area')))
        except:
            self.fail('Header not found or not visible')

        # Check Accept Cookies button
        try:
            accept_cookies_button = self.wait.until(EC.visibility_of_element_located((By.ID, 'rcc-confirm-button')))
        except:
            self.fail('Accept Cookies button not found or not visible')

        # Check main navigation links
        navigation_links = ['/category/tables', '/category/chairs', '/login', '/register']
        for link in navigation_links:
            try:
                nav_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, f'//a[@href="{link}"]')))
            except:
                self.fail(f'Navigation link to {link} not found or not visible')

        # Check product list
        try:
            product_area = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'product-area')))
        except:
            self.fail('Product area not found or not visible')

        # Check newsletter subscription
        try:
            newsletter_subscription = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'subscribe-form')))
            email_field = newsletter_subscription.find_element(By.NAME, 'email')
            subscribe_button = newsletter_subscription.find_element(By.CLASS_NAME, 'button')
            self.assertTrue(email_field.is_displayed(), 'Email field not visible')
            self.assertTrue(subscribe_button.is_displayed(), 'Subscribe button not visible')
        except:
            self.fail('Newsletter subscription form not found or components missing')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()