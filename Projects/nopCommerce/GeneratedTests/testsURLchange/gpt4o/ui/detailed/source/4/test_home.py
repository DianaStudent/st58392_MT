import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class KeyUIElementsTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check header
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-upper")))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-lower")))
        except:
            self.fail("Header elements are missing or not visible.")

        # Check footer
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer-upper")))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer-lower")))
        except:
            self.fail("Footer elements are missing or not visible.")

        # Check input fields, buttons, and search
        try:
            search_box = wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
            search_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-box-button")))
            newsletter_email = wait.until(EC.visibility_of_element_located((By.ID, "newsletter-email")))
            newsletter_subscribe_button = wait.until(EC.visibility_of_element_located((By.ID, "newsletter-subscribe-button")))
        except:
            self.fail("Input fields or buttons are missing or not visible.")

        # Interact with search
        try:
            search_box.send_keys("test")
            search_button.click()
            wait.until(EC.url_contains("/search?q=test"))
        except:
            self.fail("Search interaction failed or search result page did not load.")

        # Check navigation menu
        try:
            homepage_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home page")))
            new_products_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "New products")))
            homepage_link.click()
            wait.until(EC.url_to_be("http://max/"))
        except:
            self.fail("Navigation elements are missing or not visible.")

        # Check other elements
        try:
            register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
            login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Log in")))
            topcartlink = wait.until(EC.visibility_of_element_located((By.ID, "topcartlink")))
        except:
            self.fail("Key UI elements like register, login, or cart link are missing or not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()