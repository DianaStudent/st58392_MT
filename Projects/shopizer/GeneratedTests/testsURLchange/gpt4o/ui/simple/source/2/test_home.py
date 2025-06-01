import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestShopizerUI(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")

    def test_ui_elements(self):
        driver = self.driver

        # Define a 20 second explicit wait
        wait = WebDriverWait(driver, 20)

        # Verify header logo
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.logo img")))
        except:
            self.fail("Header logo is not visible")

        # Verify navigation links
        nav_links = [
            ("/", "Home"),
            ("/category/tables", "Tables"),
            ("/category/chairs", "Chairs")
        ]

        for href, name in nav_links:
            try:
                wait.until(EC.visibility_of_element_located((By.XPATH, f"//nav//a[@href='{href}' and text()='{name}']")))
            except:
                self.fail(f"Navigation link '{name}' is not visible")

        # Verify 'Accept cookies' button
        try:
            wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
        except:
            self.fail("'Accept cookies' button is not visible")

        # Verify 'Shop Now' button in the banner
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Shop Now']")))
        except:
            self.fail("'Shop Now' button is not visible")

        # Verify 'Featured Products' section title
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Featured Products']")))
        except:
            self.fail("'Featured Products' section title is not visible")

        # Verify 'Subscribe to our newsletter!' text
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Subscribe to our newsletter!']")))
        except:
            self.fail("'Subscribe to our newsletter!' text is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()