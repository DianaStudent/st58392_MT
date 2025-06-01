import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestLoginPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/login?returnUrl=%2F")
        self.driver.maximize_window()

    def test_ui_elements_present_and_visible(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header elements
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
        except:
            self.fail("Header not visible")

        # Check logo
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-logo")))
        except:
            self.fail("Logo not visible")

        # Check navigation links
        nav_links = ['Home page', 'New products', 'Search', 'My account', 'Blog', 'Contact us']
        for link_text in nav_links:
            try:
                wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
            except:
                self.fail(f"Navigation link '{link_text}' not visible")

        # Check "Welcome, Please Sign In!" title
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Welcome, Please Sign In!']")))
        except:
            self.fail("Title 'Welcome, Please Sign In!' not visible")

        # Check email and password fields
        form_fields = [('email', By.ID, 'Email'), ('password', By.ID, 'Password')]
        for name, by, value in form_fields:
            try:
                wait.until(EC.visibility_of_element_located((by, value)))
            except:
                self.fail(f"Form field '{name}' not visible")

        # Check "Login" button
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'login-button')))
        except:
            self.fail("Login button not visible")

        # Check "Register" button
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'register-button')))
        except:
            self.fail("Register button not visible")

        # Check "Search" functionality
        try:
            wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
        except:
            self.fail("Search input box not visible")
        
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-box-button")))
        except:
            self.fail("Search button not visible")
        
        # Check footer
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))
        except:
            self.fail("Footer not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()