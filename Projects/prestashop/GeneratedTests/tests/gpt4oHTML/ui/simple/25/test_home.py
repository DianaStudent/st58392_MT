import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestDemoWebsite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_ui_components(self):
        driver = self.driver
        wait = self.wait

        # Check Header Components
        try:
            # Check if logo is present
            logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1 img.logo")))
        except:
            self.fail("Logo is not present or visible")

        # Check Navigation Links
        try:
            clothes_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#category-3 a[href='http://localhost:8080/en/3-clothes']")))
        except:
            self.fail("Clothes link is not present or visible")

        try:
            accessories_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#category-6 a[href='http://localhost:8080/en/6-accessories']")))
        except:
            self.fail("Accessories link is not present or visible")

        try:
            art_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#category-9 a[href='http://localhost:8080/en/9-art']")))
        except:
            self.fail("Art link is not present or visible")

        # Check User Access Links
        try:
            login_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art']")))
        except:
            self.fail("Login link is not present or visible")

        try:
            register_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/registration']")))
        except:
            self.fail("Register link is not present or visible")

        # Check Search Widget
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#search_widget input[type='text'][name='s']")))
        except:
            self.fail("Search input field is not present or visible")

        # Check Product Listings
        try:
            products = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".products .js-product")))
        except:
            self.fail("Product listings are not present or visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()