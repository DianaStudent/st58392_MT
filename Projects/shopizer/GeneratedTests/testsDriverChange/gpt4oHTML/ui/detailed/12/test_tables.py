import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        # Setup ChromeDriver using webdriver-manager
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_structure_and_elements(self):
        driver = self.driver

        # Check header visibility
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header.header-area")))
        except:
            self.fail("Header is not visible")

        # Check footer visibility
        try:
            footer = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer.footer-area")))
        except:
            self.fail("Footer is not visible")

        # Check navigation links visibility
        try:
            nav_home = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            nav_tables = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            nav_chairs = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
        except:
            self.fail("Navigation links are not visible")

        # Check button for cookie consent
        try:
            cookie_accept_btn = self.wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            cookie_accept_btn.click()
        except:
            self.fail("Cookie consent button is missing or not clickable")

        # Check presence of products section
        try:
            product_section = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shop-area")))
        except:
            self.fail("Products section is missing")

        # Check visibility of account and cart buttons
        try:
            account_btn = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".account-setting-active")))
            cart_btn = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".icon-cart")))
        except:
            self.fail("Account or Cart buttons are missing")

        # Check interactive elements within product listings
        product_actions = driver.find_elements(By.CSS_SELECTOR, ".product-action button")
        if not product_actions:
            self.fail("Product action buttons (Add to cart, Quick View) are missing or not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()