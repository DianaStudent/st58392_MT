import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestRegistrationPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/registration")
    
    def test_ui_components(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Check the presence of header elements
        try:
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
            nav = header.find_element(By.CLASS_NAME, "header-nav")
            self.assertIsNotNone(nav)
        except Exception:
            self.fail("Header or nav elements are not present or visible.")
        
        # Check the main form components
        try:
            main_form = wait.until(EC.visibility_of_element_located((By.ID, "customer-form")))
            
            # Check first name field
            firstname_field = main_form.find_element(By.ID, "field-firstname")
            self.assertIsNotNone(firstname_field)
            
            # Check last name field
            lastname_field = main_form.find_element(By.ID, "field-lastname")
            self.assertIsNotNone(lastname_field)

            # Check email field
            email_field = main_form.find_element(By.ID, "field-email")
            self.assertIsNotNone(email_field)

            # Check password field
            password_field = main_form.find_element(By.ID, "field-password")
            self.assertIsNotNone(password_field)

            # Check the submit button
            submit_button = main_form.find_element(By.CSS_SELECTOR, "button[type='submit']")
            self.assertIsNotNone(submit_button)
        except Exception:
            self.fail("Main form components are not present or visible.")
        
        # Check links to other sections
        try:
            home_link = driver.find_element(By.CSS_SELECTOR, "a[href='http://localhost:8080/en/']")
            clothes_link = driver.find_element(By.CSS_SELECTOR, "a[href='http://localhost:8080/en/3-clothes']")
            accessories_link = driver.find_element(By.CSS_SELECTOR, "a[href='http://localhost:8080/en/6-accessories']")
            art_link = driver.find_element(By.CSS_SELECTOR, "a[href='http://localhost:8080/en/9-art']")
            login_link = driver.find_element(By.CSS_SELECTOR, "a[href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art']")
            register_link = driver.find_element(By.CSS_SELECTOR, "a[href='http://localhost:8080/en/registration']")

            self.assertIsNotNone(home_link)
            self.assertIsNotNone(clothes_link)
            self.assertIsNotNone(accessories_link)
            self.assertIsNotNone(art_link)
            self.assertIsNotNone(login_link)
            self.assertIsNotNone(register_link)
        except Exception:
            self.fail("One or more section links are not present or visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()