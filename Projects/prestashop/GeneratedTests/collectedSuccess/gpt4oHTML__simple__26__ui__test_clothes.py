from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestUIComponents(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.base_url = "http://localhost:8080/en/"
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Navigate to home page
        driver.get(self.base_url)

        # Check main UI components on home page
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header#header")))
        except:
            self.fail("Header is not present or visible on the home page")

        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.header-banner")))
        except:
            self.fail("Header banner is not present or visible on the home page")

        try:
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Contact us")))
        except:
            self.fail("Contact us link is not present or visible on the home page")

        try:
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
        except:
            self.fail("Sign in link is not present or visible on the home page")

        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.blockcart.cart-preview")))
        except:
            self.fail("Cart preview is not present or visible on the home page")

        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div#search_widget input[type='text']")))
        except:
            self.fail("Search input is not present or visible on the home page")

        # Check category links
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/3-clothes']")))
        except:
            self.fail("Clothes category link is not present or visible on the home page")

        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/6-accessories']")))
        except:
            self.fail("Accessories category link is not present or visible on the home page")

        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/9-art']")))
        except:
            self.fail("Art category link is not present or visible on the home page")

        # Navigate to clothes page
        driver.find_element(By.CSS_SELECTOR, "a[href='http://localhost:8080/en/3-clothes']").click()

        # Check main UI components on clothes page
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "section#main h1.h1")))
        except:
            self.fail("H1 title is not present or visible on the clothes page")

        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div#js-product-list")))
        except:
            self.fail("Product list is not present or visible on the clothes page")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()