import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestWebsiteUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header
        header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-area")))
        self.assertIsNotNone(header, "Header is not present or visible")

        # Check footer
        footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer-area")))
        self.assertIsNotNone(footer, "Footer is not present or visible")

        # Check navigation menu items
        nav_home = wait.until(EC.visibility_of_element_located((By.XPATH, "//ul/li/a[text()='Home']")))
        self.assertIsNotNone(nav_home, "Home link is not present or visible")

        nav_tables = wait.until(EC.visibility_of_element_located((By.XPATH, "//ul/li/a[text()='Tables']")))
        self.assertIsNotNone(nav_tables, "Tables link is not present or visible")

        nav_chairs = wait.until(EC.visibility_of_element_located((By.XPATH, "//ul/li/a[text()='Chairs']")))
        self.assertIsNotNone(nav_chairs, "Chairs link is not present or visible")

        # Check buttons
        accept_cookies_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
        self.assertIsNotNone(accept_cookies_button, "Accept cookies button is not present or visible")
        accept_cookies_button.click()

        # Check cart button
        cart_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "icon-cart")))
        self.assertIsNotNone(cart_button, "Cart button is not present or visible")
        cart_button.click()

        # Verify empty cart message
        empty_cart_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[text()='No items added to cart']")))
        self.assertIsNotNone(empty_cart_message, "Empty cart message is not displayed")

        # Verify input field in footer subscribe section
        email_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='email']")))
        self.assertIsNotNone(email_input, "Email input is not present or visible")

        # Verify subscribe button in footer
        subscribe_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "button")))
        self.assertIsNotNone(subscribe_button, "Subscribe button is not present or visible")

        # Failing the test if any step above did not find an element
        missing_elements = []
        elements_to_check = [header, footer, nav_home, nav_tables, nav_chairs, accept_cookies_button, cart_button, email_input, subscribe_button]
        elements_names = ["Header", "Footer", "Home Link", "Tables Link", "Chairs Link", "Accept Cookies Button", "Cart Button", "Email Input", "Subscribe Button"]

        for index, element in enumerate(elements_to_check):
            if element is None:
                missing_elements.append(elements_names[index])

        if missing_elements:
            self.fail(f"The following UI elements are missing or not visible: {', '.join(missing_elements)}")

if __name__ == "__main__":
    unittest.main()