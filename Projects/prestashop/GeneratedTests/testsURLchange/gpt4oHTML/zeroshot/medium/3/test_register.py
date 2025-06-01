import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string


class TestRegisterProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def test_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Step 2: Click on the login link in the top menu
        login_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign in")))
        self.assertTrue(login_link, "Login link not found")
        login_link.click()

        # Step 3: Click on the register link on the login page
        register_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "No account? Create one here")))
        self.assertTrue(register_link, "Register link not found")
        register_link.click()

        # Step 4: Fill in the registration form fields
        gender_mr = wait.until(EC.presence_of_element_located((By.ID, "field-id_gender-1")))
        gender_mr.click()
        
        first_name_input = wait.until(EC.presence_of_element_located((By.ID, "field-firstname")))
        first_name_input.send_keys("Test")
        
        last_name_input = wait.until(EC.presence_of_element_located((By.ID, "field-lastname")))
        last_name_input.send_keys("User")
        
        email = f"test_{''.join(random.choices(string.ascii_lowercase, k=6))}@user.com"
        email_input = wait.until(EC.presence_of_element_located((By.ID, "field-email")))
        email_input.send_keys(email)
        
        password_input = wait.until(EC.presence_of_element_located((By.ID, "field-password")))
        password_input.send_keys("test@user1")
        
        birthday_input = wait.until(EC.presence_of_element_located((By.ID, "field-birthday")))
        birthday_input.send_keys("05/31/1970")

        # Step 5: Check required checkboxes
        terms_checkbox = wait.until(EC.presence_of_element_located((By.NAME, "psgdpr")))
        terms_checkbox.click()

        privacy_checkbox = wait.until(EC.presence_of_element_located((By.NAME, "customer_privacy")))
        privacy_checkbox.click()

        # Step 6: Submit the form
        submit_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.btn-primary.form-control-submit")))
        submit_button.click()

        # Step 7: Confirm success by checking for the presence of "Sign out" in the top bar
        sign_out_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign out")))
        self.assertTrue(sign_out_link, "Sign out text not found")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()