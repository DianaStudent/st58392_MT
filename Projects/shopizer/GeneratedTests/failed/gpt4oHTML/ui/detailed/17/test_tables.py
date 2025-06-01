from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService


class UITestCase(unittest.TestCase):
    def setUp(self):
        # Setup Chrome driver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def tearDown(self):
        # Tear down the driver
        self.driver.quit()

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Check for header visibility
        header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header.header-area")))
        if not header.is_displayed():
            self.fail("Header is not visible")

        # Check for footer visibility
        footer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer.footer-area")))
        if not footer.is_displayed():
            self.fail("Footer is not visible")

        # Check for navigation links visibility (Home, Tables, Chairs, Login, Register)
        nav_links = [
            "//a[@href='/']",
            "//a[@href='/category/tables']",
            "//a[@href='/category/chairs']",
            "//a[@href='/login']",
            "//a[@href='/register']"
        ]
        for link in nav_links:
            elem = wait.until(EC.visibility_of_element_located((By.XPATH, link)))
            if not elem.is_displayed():
                self.fail(f"Navigation link {link} is not visible")

        # Check Cookie Consent button presence and interaction
        cookie_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
        if not cookie_button.is_displayed():
            self.fail("Cookie consent button is not visible")
        
        cookie_button.click()
        WebDriverWait(driver, 5).until(EC.invisibility_of_element(cookie_button), "Cookie consent button did not disappear after clicking")

        # Check for Subscribe section presence in the footer for form input visibility
        footer_subscription = driver.find_element(By.CSS_SELECTOR, "div.footer-widget.mb-30.contain input.email")
        if not footer_subscription.is_displayed():
            self.fail("Subscription input field is not visible")

        # Check visibility and interaction of Add to Cart buttons
        cart_buttons = driver.find_elements(By.XPATH, "//button[contains(text(),'Add to cart')]")
        for button in cart_buttons:
            if not button.is_displayed():
                self.fail("Add to Cart button is not visible")
            button.click()

        # Check for visual reaction (e.g., cart count changes). This part would be more advanced.

        # Ensure all elements are present and visible
        if not footer_subscription.is_displayed() or len(cart_buttons) == 0:
            self.fail("Required UI elements are missing or not interactive")

if __name__ == "__main__":
    unittest.main()