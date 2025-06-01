from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class ShopTester(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Verify header is visible
        header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header-area')))
        self.assertTrue(header.is_displayed(), "Header is not visible")

        # Verify footer is visible
        footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'footer-area')))
        self.assertTrue(footer.is_displayed(), "Footer is not visible")

        # Verify main menu links
        home_link = wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@href="/"]')))
        self.assertTrue(home_link.is_displayed(), "Home link is not visible")

        tables_link = wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@href="/category/tables"]')))
        self.assertTrue(tables_link.is_displayed(), "Tables link is not visible")

        chairs_link = wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@href="/category/chairs"]')))
        self.assertTrue(chairs_link.is_displayed(), "Chairs link is not visible")

        # Verify login and register links
        login_link = wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@href="/login"]')))
        self.assertTrue(login_link.is_displayed(), "Login link is not visible")

        register_link = wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@href="/register"]')))
        self.assertTrue(register_link.is_displayed(), "Register link is not visible")

        # Verify product and actions
        product_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@href="/product/olive-table"]')))
        self.assertTrue(product_button.is_displayed(), "Product button is not visible")
        
        # Interact with UI elements
        accept_cookies_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
        accept_cookies_button.click()

        # Verify if other elements react visually
        cart_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'icon-cart')))
        self.assertTrue(cart_button.is_displayed(), "Cart button is not visible")

        # Add assertions for other elements if needed

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()