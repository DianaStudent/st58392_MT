from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService

class TestShopizerUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header elements
        try:
            header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header.header-area")))
        except:
            self.fail("Header is missing.")

        # Check footer elements
        try:
            footer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer.footer-area")))
        except:
            self.fail("Footer is missing.")

        # Check navigation links
        try:
            nav_home = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            nav_tables = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            nav_chairs = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
        except:
            self.fail("One or more navigation links are missing.")

        # Check language dropdown
        try:
            language_dropdown = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".language-style > span")))
        except:
            self.fail("Language dropdown is missing.")

        # Check cookie consent button
        try:
            cookie_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            cookie_button.click()
        except:
            self.fail("Cookie consent button is missing or not functional.")

        # Check product grid and essential product actions
        try:
            product_grid = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".grid.three-column")))
            product_add_to_cart_buttons = product_grid.find_elements(By.CSS_SELECTOR, ".pro-cart button")
            for button in product_add_to_cart_buttons:
                self.assertTrue(button.is_displayed(), "Add to cart button is not visible.")
        except:
            self.fail("Product grid or actions are missing.")

        # Check if login and register buttons are present in dropdown
        try:
            account_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".account-setting-active")))
            account_button.click()
            login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
            register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
        except:
            self.fail("Login or Register links are missing.")

        # Check subscription email field
        try:
            subscription_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='email']")))
            subscription_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.button")))
            self.assertTrue(subscription_field.is_displayed(), "Subscription email field is not visible.")
            self.assertTrue(subscription_button.is_displayed(), "Subscription button is not visible.")
        except:
            self.fail("Subscription field or button is missing.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()