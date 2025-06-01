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
        self.driver.get("http://max/")
        self.driver.maximize_window()
    
    def test_ui_elements(self):
        driver = self.driver
        
        # Wait and check the header
        try:
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, 'header')))
        except:
            self.fail("Header is not visible")
        
        # Check the footer
        try:
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, 'footer')))
        except:
            self.fail("Footer is not visible")
        
        # Check the main navigation links
        try:
            home_link = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "Home page")))
            new_products_link = driver.find_element(By.LINK_TEXT, "New products")
            search_link = driver.find_element(By.LINK_TEXT, "Search")
        except:
            self.fail("Navigation links are not visible")
        
        # Check the search input and button
        try:
            search_input = driver.find_element(By.ID, 'small-searchterms')
            search_button = driver.find_element(By.CLASS_NAME, "search-box-button")
            self.assertTrue(search_input.is_displayed() and search_button.is_displayed())
        except:
            self.fail("Search input or button is not visible")
        
        # Interact with search button
        search_input.send_keys("test")
        search_button.click()
        
        # Verify search redirect
        WebDriverWait(driver, 20).until(EC.url_contains("search?q=test"))
        
        # Check the login and register links
        try:
            login_link = driver.find_element(By.LINK_TEXT, "Log in")
            register_link = driver.find_element(By.LINK_TEXT, "Register")
            self.assertTrue(login_link.is_displayed() and register_link.is_displayed())
        except:
            self.fail("Login or Register link is not visible")
        
        # Check the cart visibility
        try:
            cart_link = driver.find_element(By.CLASS_NAME, "ico-cart")
            self.assertTrue(cart_link.is_displayed())
        except:
            self.fail("Cart link is not visible")
        
        # Check the wishlist visibility
        try:
            wishlist_link = driver.find_element(By.CLASS_NAME, "ico-wishlist")
            self.assertTrue(wishlist_link.is_displayed())
        except:
            self.fail("Wishlist link is not visible")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()