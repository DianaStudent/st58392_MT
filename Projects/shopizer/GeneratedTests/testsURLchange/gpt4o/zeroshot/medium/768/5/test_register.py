import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class TestUserRegistration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.service = Service(ChromeDriverManager().install())
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.maximize_window()
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()
        
    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies
        wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))).click()

        # Click on the account button and select "Register"
        account_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".account-setting-active")))
        account_button.click()
        
        register_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register")))
        register_link.click()

        # Fill the registration form
        email_field = wait.until(EC.presence_of_element_located((By.NAME, "email")))
        email = f"test_{int(time.time())}@example.com"
        email_field.send_keys(email)

        password_field = driver.find_element(By.NAME, "password")
        password_field.send_keys("test**11")

        repeat_password_field = driver.find_element(By.NAME, "repeatPassword")
        repeat_password_field.send_keys("test**11")

        first_name_field = driver.find_element(By.NAME, "firstName")
        first_name_field.send_keys("Test")

        last_name_field = driver.find_element(By.NAME, "lastName")
        last_name_field.send_keys("User")

        # Select Country and State
        country_dropdown = driver.find_elements(By.TAG_NAME, "select")[0]
        action = ActionChains(driver)
        action.move_to_element(country_dropdown).click().send_keys("Canada").send_keys(Keys.ENTER).perform()

        state_dropdown = driver.find_elements(By.TAG_NAME, "select")[1]
        action.move_to_element(state_dropdown).click().send_keys("Quebec").send_keys(Keys.ENTER).perform()

        # Submit the registration form
        register_button = driver.find_element(By.CSS_SELECTOR, ".button-box button[type='submit']")
        register_button.click()

        # Confirm success by checking redirection to "/my-account"
        wait.until(EC.url_contains("/my-account"))
        current_url = driver.current_url

        if not "/my-account" in current_url:
            self.fail("Did not redirect to /my-account")

        # Assert URL confirmation
        self.assertIn("/my-account", current_url)

if __name__ == "__main__":
    unittest.main()