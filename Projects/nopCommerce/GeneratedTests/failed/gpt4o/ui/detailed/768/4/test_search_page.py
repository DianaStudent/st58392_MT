from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService

class TestPageElements(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)

    def test_page_elements(self):
        driver = self.driver
        driver.get("http://max/")
        
        # Wait setup
        wait = WebDriverWait(driver, 20)
        
        # Check header
        header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
        self.assertIsNotNone(header, "Header is not visible")
        
        # Check footer
        footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))
        self.assertIsNotNone(footer, "Footer is not visible")
        
        # Check search box
        search_box = wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
        self.assertIsNotNone(search_box, "Search box is not visible")
        
        # Check search button
        search_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "button-1.search-box-button")))
        self.assertIsNotNone(search_button, "Search button is not visible")
        
        # Check and click the register link
        register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
        self.assertIsNotNone(register_link, "Register link is not visible")
        register_link.click()
        
        # Wait for the register page
        wait.until(EC.url_contains("register?returnUrl"))
        
        # Check and click the login link
        driver.get("http://max/")
        login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Log in")))
        self.assertIsNotNone(login_link, "Login link is not visible")
        login_link.click()
        
        # Wait for the login page
        wait.until(EC.url_contains("login?returnUrl"))
        
        # Check search input in search page
        driver.get("http://max/search")
        search_input = wait.until(EC.visibility_of_element_located((By.ID, "q")))
        self.assertIsNotNone(search_input, "Search input is not visible on search page")
        
        # Check search button on search page
        search_page_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "button-1.search-button")))
        self.assertIsNotNone(search_page_button, "Search button is not visible on search page")
        
        # Check the presence of product items
        product_items = driver.find_elements(By.CLASS_NAME, "product-item")
        if not product_items:
            self.fail("No product items found on the page")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()