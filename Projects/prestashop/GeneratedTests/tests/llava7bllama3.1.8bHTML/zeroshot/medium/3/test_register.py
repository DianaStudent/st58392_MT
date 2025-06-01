from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from urllib.parse import urlsplit, parse_qs

class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:5000")

    def tearDown(self):
        self.driver.quit()

    def test_registration(self):
        # 1. Open the home page.
        self.driver.get("http://localhost:5000")

        # 2. Click on the login link in the top menu.
        login_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/login']")))
        login_link.click()

        # 3. Click on the register link on the login page.
        register_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/register']")))
        register_link.click()

        # 4. Fill in the registration form fields:
        gender_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "gender")))
        gender_input.send_keys("male")

        first_name_input = self.driver.find_element(By.XPATH, "//input[@data-name='first_name']")
        first_name_input.send_keys("Test")

        last_name_input = self.driver.find_element(By.XPATH, "//input[@data-name='last_name']")
        last_name_input.send_keys("User")

        email_input = self.driver.find_element(By.ID, "email")
        email_input.send_keys(f"test_{self.random_string(6)}@user.com")

        password_input = self.driver.find_element(By.XPATH, "//input[@data-name='password']")
        password_input.send_keys("test@user1")

        birthday_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "birthday")))
        birthday_input.send_keys("1990-01-01")

        # 5. Check required checkboxes.
        checkbox = self.driver.find_element(By.XPATH, "//input[@data-name='terms']")
        if not checkbox.is_selected():
            checkbox.click()

        # 6. Submit the form.
        submit_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        submit_button.click()

        # 7. Confirm success by checking for the presence of "Sign out" in the top bar.
        sign_out_link = self.driver.find_element(By.XPATH, "//a[text()='Sign out']")
        self.assertTrue(sign_out_link.is_displayed())

    @staticmethod
    def random_string(n):
        return ''.join([chr(random.randint(97, 122)) for _ in range(n)])

if __name__ == "__main__":
    unittest.main()