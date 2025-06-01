import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestHomePageUI(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/")

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Check for header elements
        try:
            header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
            self.assertIsNotNone(header)
        except:
            self.fail("Header not found")

        # Check for Register and Login links
        try:
            register_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.ico-register")))
            self.assertIsNotNone(register_link)
            
            login_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.ico-login")))
            self.assertIsNotNone(login_link)
        except:
            self.fail("Register or Login link not found")
        
        # Check for Shopping cart link
        try:
            cart_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.ico-cart")))
            self.assertIsNotNone(cart_link)
        except:
            self.fail("Shopping cart link not found")

        # Check for search box and button
        try:
            search_box = wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
            self.assertIsNotNone(search_box)
            
            search_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.search-box-button")))
            self.assertIsNotNone(search_button)
        except:
            self.fail("Search box or search button not found")

        # Check for footer elements
        try:
            footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))
            self.assertIsNotNone(footer)
        except:
            self.fail("Footer not found")
        
        # Check for the welcome message
        try:
            welcome_message = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "topic-block-title")))
            self.assertIsNotNone(welcome_message)
        except:
            self.fail("Welcome message not found")

if __name__ == "__main__":
    unittest.main()