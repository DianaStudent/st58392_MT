import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

class TestHomePageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_main_ui_components(self):
        driver = self.driver
        wait = self.wait

        # Check if the header is present
        try:
            header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header')))
        except TimeoutException:
            self.fail("Header is not present or not visible")

        # Check if the Register and Login links are present
        try:
            register_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.ico-register')))
            login_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.ico-login')))
        except TimeoutException:
            self.fail("Register or Login link is not present or not visible")

        # Check if the search form is present
        try:
            search_box = wait.until(EC.visibility_of_element_located((By.ID, 'small-searchterms')))
            search_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-box-button')))
        except TimeoutException:
            self.fail("Search form or button is not present or not visible")

        # Check if the shopping cart link is present
        try:
            cart_link = wait.until(EC.visibility_of_element_located((By.ID, 'topcartlink')))
        except TimeoutException:
            self.fail("Shopping cart link is not present or not visible")

        # Check if the newsletter subscription elements are present
        try:
            newsletter_email = wait.until(EC.visibility_of_element_located((By.ID, 'newsletter-email')))
            newsletter_subscribe_button = wait.until(EC.visibility_of_element_located((By.ID, 'newsletter-subscribe-button')))
        except TimeoutException:
            self.fail("Newsletter email field or subscribe button is not present or not visible")

        # Check footer components
        try:
            footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'footer')))
            footer_info = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'footer-info')))
        except TimeoutException:
            self.fail("Footer components are not present or not visible")

if __name__ == "__main__":
    unittest.main()