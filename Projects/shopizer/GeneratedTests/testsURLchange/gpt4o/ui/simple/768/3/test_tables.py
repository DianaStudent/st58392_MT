import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestShopUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check header elements
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header.header-area")))
        except:
            self.fail("Header not found or not visible")

        # Check menu links
        try:
            home_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            tables_link = driver.find_element(By.LINK_TEXT, "Tables")
            chairs_link = driver.find_element(By.LINK_TEXT, "Chairs")
        except:
            self.fail("Menu links not found or not visible")

        # Check language dropdown
        try:
            language_dropdown = driver.find_element(By.CSS_SELECTOR, ".same-language-currency.language-style")
        except:
            self.fail("Language dropdown not found or not visible")

        # Check login and register links in account settings
        try:
            account_button = driver.find_element(By.CSS_SELECTOR, ".account-setting-active")
            account_button.click()
            login_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
            register_link = driver.find_element(By.LINK_TEXT, "Register")
        except:
            self.fail("Login/Register links not found or not visible")

        # Check cart icon
        try:
            cart_icon = driver.find_element(By.CSS_SELECTOR, ".icon-cart")
        except:
            self.fail("Cart icon not found or not visible")

        # Check product elements
        try:
            product_images = driver.find_elements(By.CSS_SELECTOR, ".product-img")
            if not product_images:
                self.fail("Product images not found or not visible")
        except:
            self.fail("Product images not found or not visible")

        # Check footer elements
        try:
            footer = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer.footer-area")))
        except:
            self.fail("Footer not found or not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()