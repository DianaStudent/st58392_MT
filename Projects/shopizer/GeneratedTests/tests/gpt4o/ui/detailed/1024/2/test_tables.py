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
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        
        # Ensure header is present and visible
        header = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header.header-area")))
        self.assertIsNotNone(header, "Header is missing.")
        
        # Ensure navigation links are present and visible
        for link_text in ["Home", "Tables", "Chairs"]:
            nav_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
            self.assertIsNotNone(nav_link, f"Navigation link '{link_text}' is missing.")
        
        # Ensure footer is present and visible
        footer = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer.footer-area")))
        self.assertIsNotNone(footer, "Footer is missing.")
        
        # Check for presence and visibility of main buttons and fields
        accept_cookies_btn = self.wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
        self.assertIsNotNone(accept_cookies_btn, "Accept cookies button is missing.")
        
        # Interact with the "Accept cookies" button
        accept_cookies_btn.click()
        
        # Confirm that UI elements react visually
        products = self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".product-wrap")))
        self.assertTrue(len(products) > 0, "Products are missing from the UI.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()