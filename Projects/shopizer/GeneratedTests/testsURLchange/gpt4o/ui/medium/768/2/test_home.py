import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class TestShopUI(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.wait = WebDriverWait(self.driver, 20)
        
    def tearDown(self):
        self.driver.quit()

    def test_ui_elements_presence(self):
        driver = self.driver
        driver.get("http://localhost/")
        
        # Check navigation links
        for link_text in ["Home", "Tables", "Chairs", "Login", "Register"]:
            try:
                element = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
            except:
                self.fail(f"Navigation link '{link_text}' not found or not visible.")
        
        # Check form fields and buttons
        try:
            email_input = self.wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//input[@type='email' and @placeholder='Email address']")))
        except:
            self.fail("Email input field not found or not visible.")
        
        try:
            subscribe_button = self.wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//button[text()='Subscribe']")))
        except:
            self.fail("Subscribe button not found or not visible.")

        # Check interactive elements
        self._check_cookie_consent()
        self._check_add_to_cart_functionality()

    def _check_cookie_consent(self):
        try:
            consent_button = self.wait.until(EC.visibility_of_element_located(
                (By.ID, "rcc-confirm-button")))
            consent_button.click()
        except:
            self.fail("Cookie consent button not found or not visible.")

    def _check_add_to_cart_functionality(self):
        try:
            add_to_cart_button = self.wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//button[@title='Add to cart']")))
            add_to_cart_button.click()
        except:
            self.fail("Add to cart button not found or not visible.")

        try:
            cart_count = self.wait.until(EC.visibility_of_element_located(
                (By.CLASS_NAME, "count-style")))
            self.assertEqual(cart_count.text, "1", "Cart count did not update after add to cart.")
        except:
            self.fail("Cart count not updated or not found.")

if __name__ == "__main__":
    unittest.main()