import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header elements
        try:
            header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
        except:
            self.fail("Header not found or not visible")

        # Check main navigation links
        try:
            nav_links = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "top-menu")))
        except:
            self.fail("Navigation links not found or not visible")

        # Check search elements
        try:
            search_box = wait.until(EC.visibility_of_element_located((By.ID, "small-search-box-form")))
            search_input = driver.find_element(By.ID, "small-searchterms")
            search_button = driver.find_element(By.CLASS_NAME, "search-box-button")
        except:
            self.fail("Search elements not found or not visible")

        # Check footer elements
        try:
            footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))
        except:
            self.fail("Footer not found or not visible")

        # Check registration and login links
        try:
            register_link = driver.find_element(By.CLASS_NAME, "ico-register")
            login_link = driver.find_element(By.CLASS_NAME, "ico-login")
        except:
            self.fail("Register/Login links not found or not visible")
        
        # Interact with search field
        try:
            search_input.send_keys("Test")
            search_button.click()
            # Wait for the redirect
            wait.until(EC.title_contains("Search"))
        except:
            self.fail("Search operation failed")

        # Check that the flyout cart appears after hover
        try:
            top_cart_link = driver.find_element(By.ID, "topcartlink")
            webdriver.ActionChains(driver).move_to_element(top_cart_link).perform()
            flyout_cart = wait.until(EC.visibility_of_element_located((By.ID, "flyout-cart")))
        except:
            self.fail("Flyout cart not visible on hover")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()