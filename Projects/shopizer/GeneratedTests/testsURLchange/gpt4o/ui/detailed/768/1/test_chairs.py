import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Verify header elements
        header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header.header-area")))
        self.assertIsNotNone(header, "Header is not visible")

        # Verify navigation links
        nav_links = driver.find_elements(By.CSS_SELECTOR, "div.main-menu ul li a")
        expected_links = ["/", "/category/tables", "/category/chairs"]
        for link in expected_links:
            self.assertTrue(any(link in a.get_attribute("href") for a in nav_links), f"Navigation link for {link} is missing")

        # Verify footer
        footer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer.footer-area")))
        self.assertIsNotNone(footer, "Footer is not visible")

        # Verify buttons
        cookie_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
        self.assertTrue(cookie_button.is_displayed(), "Cookie consent button is not visible")

        # Interact with the button and verify it's clickable
        cookie_button.click()

        # Verify presence of product sections
        products = driver.find_elements(By.CSS_SELECTOR, "div.product-wrap")
        self.assertGreater(len(products), 0, "Product sections are missing")

        # Verify login and register links in header
        account_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.account-setting-active")))
        account_button.click()
        login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
        register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
        self.assertIsNotNone(login_link, "Login link is not visible")
        self.assertIsNotNone(register_link, "Register link is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()