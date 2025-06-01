from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_presence(self):
        driver = self.driver
        
        # Check structural elements
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.ID, 'header')))
            footer = self.wait.until(EC.visibility_of_element_located((By.ID, 'footer')))
        except:
            self.fail("Header or Footer is not visible")

        # Check navigation links
        try:
            nav_clothes = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Clothes')))
            nav_accessories = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Accessories')))
            nav_art = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Art')))
        except:
            self.fail("Navigation links are not visible")

        # Check input fields and buttons
        try:
            search_field = self.wait.until(EC.visibility_of_element_located((By.NAME, 's')))
            cart_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'shopping-cart')))
            sign_in_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Sign in')))
        except:
            self.fail("One or more input fields or buttons are not visible")
        
        # Interact with key UI elements
        try:
            sign_in_link.click()
            # Confirm UI reacts visually to click
            self.wait.until(EC.visibility_of_element_located((By.NAME, 'email')))
        except:
            self.fail("Interaction with Sign in link failed or email field not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()