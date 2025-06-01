from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class LoginTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_login(self):
        driver = self.driver
        wait = self.wait

        # 1. Open the homepage.
        # Done in setUp()

        # 2. Click the login link from the top navigation.
        login_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='_desktop_user_info']//span[text()='Sign in']")))
        login_link.click()

        # 3. Wait for the login page to load.
        wait.until(EC.presence_of_element_located((By.XPATH, "//h1[text()='Log in to your account']")))
        
        # 4. Fill in the email and password fields using test credentials provided.
        email_field = wait.until(EC.element_to_be_clickable((By.ID, "field-email")))
        password_field = driver.find_element(By.ID, "field-password")
        
        if email_field is None or password_field is None:
            self.fail("Email or Password field is not present.")
        
        email = "test@user.com"
        password = "test@user1"
        
        email_field.send_keys(email)
        password_field.send_keys(password)

        # 5. Click the submit button.
        submit_button = driver.find_element(By.XPATH, "//button[@id='submit-login']")
        
        if submit_button is None:
            self.fail("Submit button is not present.")
        
        submit_button.click()

        # 6. Wait for the redirect after login.
        wait.until(EC.presence_of_element_located((By.XPATH, "//a[@class='logout hidden-sm-down']")))

        # 7. Confirm that login was successful by checking that the "Sign out" button is present in the top navigation
        sign_out_button = driver.find_element(By.XPATH, "//a[contains(@class, 'logout')]")
        username_display = driver.find_element(By.XPATH, "//a[@class='account']//span[contains(@class, 'hidden-sm-down')]")

        if sign_out_button is None or username_display is None:
            self.fail("Sign out button or Username display is not present.")

        # Confirm presence of "Sign out" and username text.
        self.assertIn("Sign out", sign_out_button.text)
        self.assertIn("test user", username_display.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()