import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/en/login")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Verify page header presence
        header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        if not header:
            self.fail("Page header is not visible")

        # Verify navigation links
        nav_links = [
            ("Home", "http://localhost:8080/en/"),
            ("Clothes", "http://localhost:8080/en/3-clothes"),
            ("Accessories", "http://localhost:8080/en/6-accessories"),
            ("Art", "http://localhost:8080/en/9-art"),
            ("Sign in", "http://localhost:8080/en/login")
        ]

        for link_text, href in nav_links:
            try:
                element = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
                self.assertEqual(element.get_attribute('href'), href)
            except Exception as e:
                self.fail(f"Navigation link {link_text} with href {href} is not visible or not correct: {str(e)}")
        
        # Verify form elements
        email_input = wait.until(EC.visibility_of_element_located((By.ID, 'field-email')))
        password_input = wait.until(EC.visibility_of_element_located((By.ID, 'field-password')))
        submit_button = wait.until(EC.visibility_of_element_located((By.ID, 'submit-login')))

        if not email_input or not password_input or not submit_button:
            self.fail("Form elements (email, password, submit) are not visible")

        # Interact with the form
        email_input.send_keys("test@example.com")
        password_input.send_keys("password")
        submit_button.click()

        # Verify the form interaction does not cause errors in UI
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'page-content')))
            # Assume page-content indicates that the page has not crashed/errors did not occur
        except Exception as e:
            self.fail(f"UI is broken after interacting with form: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()