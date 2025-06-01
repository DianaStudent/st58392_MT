import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestShopWebsite(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_ui_elements(self):
        driver = self.driver
        
        # Check visibility of header
        header = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".header-area")))
        self.assertTrue(header.is_displayed(), "Header is not visible")
        
        # Check presence and visibility of navigation links
        nav_links = {
            "home": "/",
            "tables": "/category/tables",
            "chairs": "/category/chairs"
        }
        for page, link in nav_links.items():
            try:
                nav_element = driver.find_element(By.CSS_SELECTOR, f'a[href="{link}"]')
                self.assertTrue(nav_element.is_displayed(), f"Navigation link for {page} is not visible")
            except:
                self.fail(f"Navigation link for {page} not found")
        
        # Check presence and visibility of login and register links
        auth_links = {
            "login": "/login",
            "register": "/register"
        }
        for action, link in auth_links.items():
            try:
                element = driver.find_element(By.CSS_SELECTOR, f'a[href="{link}"]')
                self.assertTrue(element.is_displayed(), f"{action.capitalize()} link is not visible")
            except:
                self.fail(f"{action.capitalize()} link not found")
        
        # Check visibility of footer
        footer = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".footer-area")))
        self.assertTrue(footer.is_displayed(), "Footer is not visible")
        
        # Check visibility and interaction with Accept Cookies button
        try:
            cookie_button = self.wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            self.assertTrue(cookie_button.is_displayed(), "Accept cookies button is not visible")
            cookie_button.click()
        except:
            self.fail("Accept cookies button not found or not clickable")
        
        # Check presence and visibility of product elements
        product_elements = driver.find_elements(By.CSS_SELECTOR, ".product-wrap")
        if not product_elements:
            self.fail("No product elements found on the page")
        for product in product_elements:
            self.assertTrue(product.is_displayed(), "Product element is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()