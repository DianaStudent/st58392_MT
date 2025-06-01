import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestUIComponents(unittest.TestCase):

    def setUp(self):
        # Set up Chrome browser
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        
        # Check header visibility
        try:
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header.header-area")))
        except:
            self.fail("Header component is missing or not visible.")
        
        # Check footer visibility
        try:
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer.footer-area")))
        except:
            self.fail("Footer component is missing or not visible.")
        
        # Check main menu presence and visibility
        try:
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.main-menu")))
        except:
            self.fail("Main menu is missing or not visible.")
        
        # Check navigation links visibility (Home, Tables, Chairs)
        navigation_links = ["Home", "Tables", "Chairs"]
        for link_text in navigation_links:
            try:
                link_element = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
                self.assertTrue(link_element.is_displayed(), f"{link_text} link is not displayed.")
            except:
                self.fail(f"Navigation link '{link_text}' is missing or not visible.")
        
        # Interact with the login link
        try:
            login_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
            login_link.click()
        except:
            self.fail("Login link is missing or could not be clicked.")
        
        # Check form fields on login page
        input_fields = ["Email address", "Password"]
        for placeholder in input_fields:
            try:
                field = self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//input[@placeholder='{placeholder}']")))
                self.assertTrue(field.is_displayed(), f"Input field '{placeholder}' is not displayed.")
            except:
                self.fail(f"Input field '{placeholder}' is missing or not visible.")

        # Check presence of register link on login page
        try:
            register_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
            self.assertTrue(register_link.is_displayed(), "Register link is not displayed.")
        except:
            self.fail("Register link on login page is missing or not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()