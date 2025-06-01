import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestShopizerUI(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait
        
        # Check for header
        header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header-area')))
        self.assertIsNotNone(header, "Header not found")

        # Check for footer
        footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'footer-area')))
        self.assertIsNotNone(footer, "Footer not found")

        # Check for main navigation links
        nav_links = {
            "Home": "/",
            "Tables": "/category/tables",
            "Chairs": "/category/chairs"
        }
        for name, href in nav_links.items():
            link = wait.until(EC.visibility_of_element_located((By.XPATH, f"//a[@href='{href}']")))
            self.assertIsNotNone(link, f"{name} link not found")

        # Check for login/register links
        auth_links = {
            "Login": "/login",
            "Register": "/register"
        }
        for name, href in auth_links.items():
            link = wait.until(EC.visibility_of_element_located((By.XPATH, f"//a[@href='{href}']")))
            self.assertIsNotNone(link, f"{name} link not found")

        # Check for product-related UI elements
        product_grid = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'shop-bottom-area')))
        self.assertIsNotNone(product_grid, "Product grid not found")

        products = driver.find_elements(By.CLASS_NAME, 'product-wrap')
        self.assertGreater(len(products), 0, "No products found")

        # Interact with the Cookie consent button
        try:
            cookie_button = wait.until(EC.element_to_be_clickable((By.ID, 'rcc-confirm-button')))
            cookie_button.click()
        except Exception as e:
            self.fail(f"Cookie consent button missing or not clickable: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()