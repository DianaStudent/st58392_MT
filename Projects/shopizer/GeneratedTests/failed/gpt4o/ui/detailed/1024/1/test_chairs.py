from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class ShopPageTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_are_present_and_visible(self):
        # Check header
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header.header-area")))
        except:
            self.fail("Header is not visible")

        # Check navigation menu
        try:
            menu = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.main-menu nav ul")))
        except:
            self.fail("Navigation menu is not visible")

        # Check footer
        try:
            footer = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer.footer-area")))
        except:
            self.fail("Footer is not visible")

        # Check language/currency, call us, and user icons
        try:
            language_currency = self.driver.find_element(By.CSS_SELECTOR, "div.language-style span")
            self.assertTrue(language_currency.is_displayed(), "Language/Currency not visible")

            call_us = self.driver.find_element(By.XPATH, "//p[contains(text(),'Call Us : 888-888-8888')]")
            self.assertTrue(call_us.is_displayed(), "Call Us text not visible")

            user_icon = self.driver.find_element(By.CSS_SELECTOR, "div.account-setting button.account-setting-active")
            self.assertTrue(user_icon.is_displayed(), "User icon not visible")
        except:
            self.fail("Header icons are not visible")

        # Check main product sections
        try:
            products = self.driver.find_elements(By.CSS_SELECTOR, "div.product-wrap")
            self.assertTrue(len(products) > 0, "No products are visible")
        except:
            self.fail("Product sections are not visible")

        # Check cart button
        try:
            cart_button = self.driver.find_element(By.CSS_SELECTOR, "button.icon-cart")
            self.assertTrue(cart_button.is_displayed(), "Cart button is not visible")
        except:
            self.fail("Cart button is not visible")

        # Check Accept Cookies button and interact
        try:
            accept_cookies = self.wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            self.assertTrue(accept_cookies.is_displayed(), "Accept Cookies button is not visible")
            accept_cookies.click()
        except:
            self.fail("Accept Cookies button is not interactable")

        # Check subscribe button
        try:
            subscribe_button = self.driver.find_element(By.CSS_SELECTOR, "button.button")
            self.assertTrue(subscribe_button.is_displayed(), "Subscribe button is not visible")
        except:
            self.fail("Subscribe button is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()