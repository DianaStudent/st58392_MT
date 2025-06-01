import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check header visibility
        header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header-area')))
        self.assertTrue(header.is_displayed(), "Header is not visible.")

        # Check navigation links visibility
        nav_links = [
            (By.LINK_TEXT, "Home"),
            (By.LINK_TEXT, "Tables"),
            (By.LINK_TEXT, "Chairs"),
        ]
        for selector in nav_links:
            element = wait.until(EC.visibility_of_element_located(selector))
            self.assertTrue(element.is_displayed(), f"{element.text} link is not visible.")

        # Check footer visibility
        footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'footer-area')))
        self.assertTrue(footer.is_displayed(), "Footer is not visible.")

        # Check buttons and other interactable elements
        accept_cookies_button = wait.until(EC.visibility_of_element_located((By.ID, 'rcc-confirm-button')))
        self.assertTrue(accept_cookies_button.is_displayed(), "Accept cookies button is not visible.")
        accept_cookies_button.click()

        # Check product presence
        product = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Olive Table')))
        self.assertTrue(product.is_displayed(), "Olive Table product link is not visible.")

        # Check Cart Button visibility
        cart_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.icon-cart')))
        self.assertTrue(cart_button.is_displayed(), "Cart button is not visible.")

        # Check form elements in footer
        email_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="email"]')))
        self.assertTrue(email_field.is_displayed(), "Email subscription field is not visible.")

        subscribe_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.button')))
        self.assertTrue(subscribe_button.is_displayed(), "Subscribe button is not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()