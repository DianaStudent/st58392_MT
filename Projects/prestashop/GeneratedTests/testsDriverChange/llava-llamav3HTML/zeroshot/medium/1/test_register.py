```
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager
import time
import re

class TestRegister(unittest.TestCase):
    def setUp(self):
        driver = webdriver.Chrome(ChromeDriverManager().get_chrome_driver_path())
        self.driver = driver

    def tearDown(self):
        self.driver.quit()

    def test_register(self):
        # Step 1: Open the home page.
        self.driver.get("http://localhost:8080/en/")

        # Step 2: Click on the login link in the top menu.
        login_link = WebDriverWait(self.driver, 20).until(EC.element_located((By.XPATH, "//a[@class='nav-link text-dark active']")))

        login_link.click()

        # Step 3: Click on the register link on the login page.
        register_link = WebDriverWait(self.driver, 20).until(EC.element_located((By.XPATH, "//a[@data-name='register-link']")))

        register_link.click()

        # Step 4: Fill in the registration form fields:
        gender = WebDriverWait(self.driver, 20).until(EC.element_located((By.XPATH, "//label[@id='gender']")))
        gender.select_by_visible_text("Male")

        first_name = WebDriverWait(self.driver, 20).until(EC.element_located((By.XPATH, "//input[@data-name='first-name']")))
        last_name = WebDriverWait(self.driver, 20).until(EC.element_located((By.XPATH, "//input[@data-name='last-name']")))
        email = WebDriverWait(self.driver, 20).until(EC.element_located((By.XPATH, "//input[@data-name='email']")))
        password = WebDriverWait(self.driver, 20).until(EC.element_located((By.XPATH, "//input[@data-name='password']")))
        birthday = WebDriverWait(self.driver, 20).until(EC.element_located((By.XPATH, "//input[@data-name='birthday']")))

        first_name.send_keys("John")
        last_name.send_keys("Doe")
        email.send_keys(f"test_{re.search(r'\d{9}\@user\.com', self.email)}")
        password.send_keys("test@user1")
        birthday.send_keys("01/02/1980")

        # Step 5: Check required checkboxes.
        checkbox1 = WebDriverWait(self.driver, 20).until(EC.element_located((By.XPATH, "//input[@data-name='check1']")))
        checkbox2 = WebDriverWait(self.driver, 20).until(EC.element_located((By.XPATH, "//input[@data-name='check2']")))

        checkbox1.click()
        checkbox2.click()

        # Step 6: Submit the form.
        submit_button = WebDriverWait(self.driver, 20).until(EC.element_located((By.XPATH, "//button[@data-name='submit-button']")))
        submit_button.click()

        # Step 7: Confirm success by checking for the presence of "Sign out" in the top bar.
        sign_out_link = WebDriverWait(self.driver, 20).until(EC.element_located((By.XPATH, "//a[@class='nav-link text-dark active']")))
        self.assertTrue(sign_out_link is not None)

if __name__ == '__main__':
    unittest.main()
```