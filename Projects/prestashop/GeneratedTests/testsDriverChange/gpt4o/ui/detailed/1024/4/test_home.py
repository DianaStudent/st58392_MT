import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestDemoPageElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Verify header is visible
        header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
        self.assertTrue(header.is_displayed(), "Header is not visible")

        # Verify footer is visible
        footer = self.wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        self.assertTrue(footer.is_displayed(), "Footer is not visible")

        # Verify navigation is visible
        nav = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-nav")))
        self.assertTrue(nav.is_displayed(), "Navigation is not visible")

        # Check input fields
        search_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "s")))
        self.assertTrue(search_input.is_displayed(), "Search input is not visible")

        # Check buttons and links
        contact_us_link = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(@href, 'contact-us')]")))
        self.assertTrue(contact_us_link.is_displayed(), "Contact Us link is not visible")

        login_link = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[@href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art']")))
        self.assertTrue(login_link.is_displayed(), "Login link is not visible")

        # Interact with elements
        cart = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart-preview .header")))
        cart.click()

        # Confirm UI reaction
        cart_icon = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping-cart")))
        self.assertTrue(cart_icon.is_displayed(), "Cart icon did not appear")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()