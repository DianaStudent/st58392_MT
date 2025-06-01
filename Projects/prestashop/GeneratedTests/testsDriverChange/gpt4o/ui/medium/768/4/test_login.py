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
        self.driver.get("http://localhost:8080/en/login")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check navigation links
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/']")))
            clothes_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']")))
            accessories_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/6-accessories']")))
            art_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']")))
            self.assertTrue(home_link.is_displayed(), "Home link is not displayed")
            self.assertTrue(clothes_link.is_displayed(), "Clothes link is not displayed")
            self.assertTrue(accessories_link.is_displayed(), "Accessories link is not displayed")
            self.assertTrue(art_link.is_displayed(), "Art link is not displayed")
            
        except Exception as e:
            self.fail(f"Navigation links missing: {e}")

        # Check login form elements
        try:
            email_input = wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
            password_input = wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
            submit_button = wait.until(EC.visibility_of_element_located((By.ID, "submit-login")))
            self.assertTrue(email_input.is_displayed(), "Email input is not displayed")
            self.assertTrue(password_input.is_displayed(), "Password input is not displayed")
            self.assertTrue(submit_button.is_displayed(), "Submit button is not displayed")
            
        except Exception as e:
            self.fail(f"Form elements missing: {e}")

        # Interact with an element
        try:
            email_input.send_keys("test@example.com")
            password_input.send_keys("password")
            submit_button.click()
            # Check if URL changes or any indication of login attempt is shown
            wait.until(EC.url_contains("http://localhost:8080/en/login"))
        except Exception as e:
            self.fail(f"Interaction with form caused error: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()