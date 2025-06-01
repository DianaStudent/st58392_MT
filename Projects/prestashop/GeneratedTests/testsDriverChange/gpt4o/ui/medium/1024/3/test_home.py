import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestDemoPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Verify navigation links are present and visible
        nav_links = [
            (By.ID, "category-3", "Clothes"),
            (By.ID, "category-6", "Accessories"),
            (By.ID, "category-9", "Art"),
        ]

        for by, value, name in nav_links:
            try:
                element = self.wait.until(EC.visibility_of_element_located((by, value)))
            except:
                self.fail(f"Navigation link for {name} not visible.")

        # Verify button links (Login and Register) are present and visible
        button_links = [
            (By.LINK_TEXT, "Sign in"),
            (By.LINK_TEXT, "Create account")
        ]

        for by, value in button_links:
            try:
                element = self.wait.until(EC.visibility_of_element_located((by, value)))
            except:
                self.fail(f"Button link with text {value} not visible.")

        # Verify search bar input is present and visible
        try:
            search_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "s")))
        except:
            self.fail("Search input not visible.")

        # Interact with the search input and verify no errors occur
        search_input.send_keys('Sample product')
        search_input.submit()

        # Verify banner is present and visible
        try:
            banner = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "banner")))
        except:
            self.fail("Banner not visible.")

        # Click on the first product quick view and verify no errors occur
        try:
            product_quick_view = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-miniature .quick-view")))
            ActionChains(driver).move_to_element(product_quick_view).click(product_quick_view).perform()
        except:
            self.fail("Quick view button for product not clickable.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()