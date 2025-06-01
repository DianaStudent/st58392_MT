import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost:8080/en/')
        self.driver.maximize_window()

    def test_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Open the home page
        wait.until(EC.presence_of_element_located((By.ID, "index")))

        # Click on the login link in the top menu
        signin_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign in")))
        signin_link.click()

        # Click on the register link on the login page
        register_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Create one here")))
        register_link.click()

        # Fill in the registration form fields
        gender_mr = wait.until(EC.presence_of_element_located((By.ID, "field-id_gender-1")))
        first_name = driver.find_element(By.ID, "field-firstname")
        last_name = driver.find_element(By.ID, "field-lastname")
        email = driver.find_element(By.ID, "field-email")
        password = driver.find_element(By.ID, "field-password")
        birthday = driver.find_element(By.ID, "field-birthday")

        gender_mr.click()
        first_name.send_keys("Test")
        last_name.send_keys("User")
        email.send_keys(f"test_{int(time.time())}@user.com")
        password.send_keys("test@user1")
        birthday.send_keys("05/31/1970")

        # Check required checkboxes
        privacy_policy = driver.find_element(By.NAME, "psgdpr")
        customer_privacy = driver.find_element(By.NAME, "customer_privacy")

        ActionChains(driver).move_to_element(privacy_policy).perform()
        privacy_policy.click()

        ActionChains(driver).move_to_element(customer_privacy).perform()
        customer_privacy.click()

        # Submit the form
        submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_button.click()

        # Confirm success by checking for the presence of "Sign out" in the top bar
        try:
            sign_out = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign out")))
            self.assertTrue(sign_out.is_displayed(), "Registration failed: 'Sign out' not visible")
        except Exception as e:
            self.fail(f"Registration failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()