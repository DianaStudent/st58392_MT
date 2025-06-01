from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestSelenium(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080/en/")  # Replace with actual URL

    def test_sign_out(self):
        # Wait for the email input field to be visible
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@type='email']"))
        )
        
        # Fill in the email field
        self.driver.find_element(By.XPATH, "//input[@type='email']").send_keys("test@user.com")

        # Wait for the password input field to be visible
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@type='password']"))
        )
        
        # Fill in the password field
        self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys("test@user1")

        # Wait for the login button to be clickable
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-name='login']"))
        )
        
        # Click on the login button
        self.driver.find_element(By.XPATH, "//button[@data-name='login']").click()

        # Wait for the sign out link to be visible
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@data-name='sign-out']"))
        )

        # Check if the sign out link is present and has text "Sign out"
        self.failUnless(EC.text_to_be_present_in_element((By.XPATH, "//a[@data-name='sign-out']"), "Sign out"))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()