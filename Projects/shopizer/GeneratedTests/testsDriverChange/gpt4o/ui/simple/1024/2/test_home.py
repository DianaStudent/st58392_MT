import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestWebsiteUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_main_ui_elements(self):
        # Check header navigation links
        try:
            header_links = ["Home", "Tables", "Chairs", "Login", "Register"]
            for link_text in header_links:
                element = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
                self.assertTrue(element.is_displayed(), f"{link_text} link not displayed")
        
            # Check 'Accept cookies' button
            accept_cookies_btn = self.wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            self.assertTrue(accept_cookies_btn.is_displayed(), "Accept cookies button not displayed")

            # Check 'Shop Now' button
            shop_now_btn = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Shop Now")))
            self.assertTrue(shop_now_btn.is_displayed(), "Shop Now button not displayed")

            # Check product images and links
            product_selectors = [
                (By.XPATH, "//a[@href='/product/olive-table']"),
                (By.XPATH, "//a[@href='/product/chair']"),
                (By.XPATH, "//a[@href='/product/chair-beige']"),
                (By.XPATH, "//a[@href='/product/genuine-chair']")
            ]
            for selector in product_selectors:
                product_element = self.wait.until(EC.visibility_of_element_located(selector))
                self.assertTrue(product_element.is_displayed(), f"Product {selector[1]} not displayed")
        
            # Check 'Subscribe' form
            subscribe_input = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.email")))
            self.assertTrue(subscribe_input.is_displayed(), "'Subscribe' email input not displayed")
            
            subscribe_btn = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.button")))
            self.assertTrue(subscribe_btn.is_displayed(), "'Subscribe' button not displayed")
        
        except Exception as e:
            self.fail(str(e))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()