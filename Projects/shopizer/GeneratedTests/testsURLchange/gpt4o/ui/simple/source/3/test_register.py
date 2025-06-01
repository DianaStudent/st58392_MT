import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestWebPageUIElements(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/login")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_ui_elements(self):
        driver = self.driver

        # Check header elements
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-area")))
        
        # Check Home link
        home_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/']")))
        self.assertTrue(home_link.is_displayed())

        # Check Tables link
        tables_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category/tables']")))
        self.assertTrue(tables_link.is_displayed())

        # Check Chairs link
        chairs_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category/chairs']")))
        self.assertTrue(chairs_link.is_displayed())
        
        # Check Login form fields
        email_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "email")))
        self.assertTrue(email_field.is_displayed())

        password_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "password")))
        self.assertTrue(password_field.is_displayed())

        repeat_password_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "repeatPassword")))
        self.assertTrue(repeat_password_field.is_displayed())
        
        # Check Register button
        register_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[span='Register']")))
        self.assertTrue(register_button.is_displayed())

        # Check footer elements
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer-area")))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()