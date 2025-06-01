import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class ShopizerUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Ensure header is present and visible
        header = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header.header-area")))
        self.assertIsNotNone(header, "Header is not present or visible.")

        # Ensure footer is present and visible
        footer = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer.footer-area")))
        self.assertIsNotNone(footer, "Footer is not present or visible.")

        # Ensure main navigation links are visible
        nav_home = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
        nav_tables = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
        nav_chairs = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))

        self.assertIsNotNone(nav_home, "Home link is not visible.")
        self.assertIsNotNone(nav_tables, "Tables link is not visible.")
        self.assertIsNotNone(nav_chairs, "Chairs link is not visible.")

        # Ensure 'Shop Now' button is present and visible
        shop_now_btn = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Shop Now")))
        self.assertIsNotNone(shop_now_btn, "'Shop Now' button is not visible.")

        # Ensure newsletter subscription input field and button are visible
        email_input = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.email")))
        subscribe_btn = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".subscribe-form-3 .button")))

        self.assertIsNotNone(email_input, "Email input is not visible.")
        self.assertIsNotNone(subscribe_btn, "Subscribe button is not visible.")

        # Interact with the cookie consent button
        cookie_btn = self.wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
        self.assertIsNotNone(cookie_btn, "Cookie consent button is not visible.")
        cookie_btn.click()

        # Confirm the cart icon is visible and has a correct item count
        cart_icon = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "icon-cart")))
        cart_count = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "count-style")))

        self.assertIsNotNone(cart_icon, "Cart icon is not visible.")
        self.assertEqual(cart_count.text, "0", "Cart count is not zero as expected.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()