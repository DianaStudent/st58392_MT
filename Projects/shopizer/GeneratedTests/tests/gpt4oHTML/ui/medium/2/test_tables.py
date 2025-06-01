import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestShopUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def test_ui_elements(self):
        driver = self.driver

        # Wait for header
        header = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "header.header-area"))
        )

        # Check navigation links
        nav_links = [
            {"name": "Home", "url": "/", "selector": "a[href='/']"},
            {"name": "Tables", "url": "/category/tables", "selector": "a[href='/category/tables']"},
            {"name": "Chairs", "url": "/category/chairs", "selector": "a[href='/category/chairs']"}
        ]
        for link in nav_links:
            element = header.find_element(By.CSS_SELECTOR, link['selector'])
            self.assertTrue(element.is_displayed(), f"{link['name']} link is not visible")

        # Check 'Accept Cookies' button
        cookies_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "rcc-confirm-button"))
        )
        self.assertTrue(cookies_button.is_displayed(), "Accept Cookies button is not visible")
        
        # Click the 'Accept Cookies' button
        cookies_button.click()

        # Check login and register links
        account_dropdown_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".same-style.account-setting button.account-setting-active"))
        )
        account_dropdown_button.click()
        
        login_link = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Login"))
        )
        self.assertTrue(login_link.is_displayed(), "Login link is not visible")

        register_link = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Register"))
        )
        self.assertTrue(register_link.is_displayed(), "Register link is not visible")
        
        # Check 'Add to cart' button for a product
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'product-wrap')]//button[contains(., 'Add to cart')]"))
        )
        self.assertTrue(add_to_cart_button.is_displayed(), "Add to cart button is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()