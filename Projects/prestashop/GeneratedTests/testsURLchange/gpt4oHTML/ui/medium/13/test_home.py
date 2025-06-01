import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check presence of main navigation links
        for href in [
            'http://localhost:8080/en/3-clothes', 
            'http://localhost:8080/en/6-accessories', 
            'http://localhost:8080/en/9-art'
        ]:
            self.assertTrue(wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, f'a[href="{href}"]'))), f'Missing link with href {href}')

        # Check presence of login and registration links
        for href in [
            'http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art', 
            'http://localhost:8080/en/registration'
        ]:
            self.assertTrue(wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, f'a[href="{href}"]'))), f'Missing link with href {href}')

        # Check presence of search input box
        self.assertTrue(wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'input[type="text"][name="s"]'))), 'Missing search input box')

        # Check presence of cart button
        self.assertTrue(wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '#_desktop_cart .shopping-cart'))), 'Missing cart icon/button')

        # Check presence of a banner
        self.assertTrue(wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '.banner img'))), 'Missing banner image')

        # Interact with an element - click 'Clothes' and check landing
        clothes_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="http://localhost:8080/en/3-clothes"]')))
        clothes_link.click()

        # Confirm the correct page has loaded by checking some element on the clothes page
        self.assertTrue(wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'h3.product-title a'))), 'Products do not appear on clothes page')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()