from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class UITest(unittest.TestCase):

    def setUp(self):
        # Setup Chrome Driver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_UI_elements(self):
        driver = self.driver

        # Assert that the page loaded and key structural elements are visible
        self.assertTrue(self.wait.until(EC.visibility_of_element_located((By.ID, "root"))))
        
        # Check headers and navigation
        header = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-area")))
        self.assertTrue(header.is_displayed(), "Header is missing or not visible")
        
        # Check footer
        footer = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer-area")))
        self.assertTrue(footer.is_displayed(), "Footer is missing or not visible")

        # Checking Accept Cookies button
        accept_button = self.wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
        self.assertTrue(accept_button.is_displayed(), "Accept Cookies button is missing or not visible")
        accept_button.click()

        # Check for main menu items
        for item in ["Home", "Tables", "Chairs"]:
            link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, item)))
            self.assertTrue(link.is_displayed(), f"{item} link is missing or not visible")

        # Check login/register links in account-dropdown
        account_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "account-setting-active")))
        account_button.click()
        
        login_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
        self.assertTrue(login_link.is_displayed(), "Login link is missing or not visible")
        
        register_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
        self.assertTrue(register_link.is_displayed(), "Register link is missing or not visible")
        
        # Product section check
        product_section = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shop-area")))
        self.assertTrue(product_section.is_displayed(), "Product section is missing or not visible")

        # Confirm visual response by clicking on product add to cart
        add_to_cart_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(@title, 'Add to cart')]")))
        self.assertTrue(add_to_cart_button.is_displayed(), "Add To Cart button is missing or not visible")
        add_to_cart_button.click()

    def tearDown(self):
        # Quit the driver
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()