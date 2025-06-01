import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

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
            clothes_link = driver.find_element(By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']")
            accessories_link = driver.find_element(By.XPATH, "//a[@href='http://localhost:8080/en/6-accessories']")
            art_link = driver.find_element(By.XPATH, "//a[@href='http://localhost:8080/en/9-art']")
        except:
            self.fail("Navigation links are missing or not visible.")

        # Check login form fields
        try:
            email_input = wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
            password_input = driver.find_element(By.ID, "field-password")
            submit_button = driver.find_element(By.ID, "submit-login")
        except:
            self.fail("Login form fields are missing or not visible.")

        # Try an interaction: click the "Sign in" button
        try:
            submit_button.click()
        except:
            self.fail("Failed to click the Sign in button.")

        # Check for a specific error or success message after clicking the button
        try:
            error_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'alert-danger')]")))
        except:
            self.fail("Error message not displayed as expected after clicking Sign in.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()