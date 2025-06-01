import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestShopizerUI(unittest.TestCase):

    def setUp(self):
        self.driver: WebDriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        driver = self.driver

        # Check for navigation links
        nav_links = [
            (By.LINK_TEXT, "Home"),
            (By.LINK_TEXT, "Tables"),
            (By.LINK_TEXT, "Chairs"),
        ]
        
        for by, value in nav_links:
            nav_element = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((by, value))
            )
            self.assertIsNotNone(nav_element, f"Navigation link '{value}' not found")

        # Check for header logo
        logo = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".logo img"))
        )
        self.assertIsNotNone(logo, "Header logo not found")

        # Check for cookie consent button
        cookie_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "rcc-confirm-button"))
        )
        self.assertIsNotNone(cookie_button, "Cookie consent button not found")

        # Accept cookies
        cookie_button.click()

        # Check for language/currency selector
        language_selector = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".same-language-currency.language-style span"))
        )
        self.assertIsNotNone(language_selector, "Language/Currency selector not found")

        # Check for cart button
        cart_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".same-style.cart-wrap.d-none.d-lg-block button.icon-cart"))
        )
        self.assertIsNotNone(cart_button, "Cart button not found")
        
        # Click 'Add to cart' for the first product
        add_to_cart_buttons = driver.find_elements(By.CSS_SELECTOR, ".pro-cart button")
        if add_to_cart_buttons:
            add_to_cart_buttons[0].click()
        else:
            self.fail("Add to cart button not found")

        # Assert that cart count is updated
        cart_count = WebDriverWait(driver, 20).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".same-style.cart-wrap.d-none.d-lg-block .count-style"), "1")
        )
        self.assertTrue(cart_count, "Cart count did not update")

if __name__ == "__main__":
    unittest.main()