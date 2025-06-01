import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_present_and_visible(self):
        driver = self.driver

        # Check header logo
        logo = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='logo']/a/img")))
        self.assertIsNotNone(logo, "Logo is missing or not visible")

        # Check navigation links
        nav_links = ["Home", "Tables", "Chairs"]
        for link_text in nav_links:
            nav_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
            self.assertIsNotNone(nav_link, f"Navigation link '{link_text}' is missing or not visible")

        # Check Account button
        account_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".account-setting button")))
        self.assertIsNotNone(account_button, "Account button is missing or not visible")

        # Check Cart button
        cart_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".icon-cart")))
        self.assertIsNotNone(cart_button, "Cart button is missing or not visible")

        # Check Cookie Consent button
        cookie_button = self.wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
        self.assertIsNotNone(cookie_button, "Cookie Accept button is missing or not visible")

        # Check Subscribe form fields
        subscribe_input = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".subscribe-form-3 input.email")))
        self.assertIsNotNone(subscribe_input, "Subscribe email input is missing or not visible")

        subscribe_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".subscribe-form-3 button.button")))
        self.assertIsNotNone(subscribe_button, "Subscribe button is missing or not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()