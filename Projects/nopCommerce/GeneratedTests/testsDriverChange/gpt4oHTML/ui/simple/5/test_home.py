import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIComponents(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_main_ui_components(self):
        driver = self.driver

        # Check if the header is present and visible
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
        except:
            self.fail("Header is not present or visible.")

        # Check if the register link is present and visible
        try:
            register_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
        except:
            self.fail("Register link is not present or visible.")

        # Check if the login link is present and visible
        try:
            login_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Log in")))
        except:
            self.fail("Log in link is not present or visible.")

        # Check if the search box is present and visible
        try:
            search_box = self.wait.until(EC.visibility_of_element_located((By.ID, "small-search-box-form")))
            search_input = self.wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
            search_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='button-1 search-box-button']")))
        except:
            self.fail("Search form or its components are not present or visible.")

        # Check if the shopping cart link is present and visible
        try:
            cart_link = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ico-cart")))
        except:
            self.fail("Shopping cart link is not present or visible.")

        # Check if the newsletter subscription field is present and visible
        try:
            newsletter_field = self.wait.until(EC.visibility_of_element_located((By.ID, "newsletter-email")))
            subscribe_button = self.wait.until(EC.visibility_of_element_located((By.ID, "newsletter-subscribe-button")))
        except:
            self.fail("Newsletter subscription field or button is not present or visible.")

        # Check if the footer is present and visible
        try:
            footer = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))
        except:
            self.fail("Footer is not present or visible.")

if __name__ == "__main__":
    unittest.main()