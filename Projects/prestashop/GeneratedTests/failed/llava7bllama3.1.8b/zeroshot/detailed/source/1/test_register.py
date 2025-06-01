from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_registration(self):
        # Step 1: Click login link
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/en/login']"))).click()

        # Step 2: Click register link on login page
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//p[@class='text-center']//a[contains(., 'Register')]"))).click()

        # Step 3: Fill in registration form
        email = f"test_{self.generate_random_string()}@user.com"
        self.driver.find_element(By.XPATH, "//input[@name='gender']").send_keys("1")  # Mr.
        self.driver.find_element(By.XPATH, "(//input[@name='first_name'])[1]").send_keys("Test")
        self.driver.find_element(By.XPATH, "(//input[@name='last_name'])[1]").send_keys("User")
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys(email)
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("test@user1")
        self.driver.find_element(By.XPATH, "(//input[@type='date'])[1]").send_keys("2000-01-01")

        # Step 4: Submit registration form
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary']"))).click()

    def tearDown(self):
        self.driver.quit()

    @staticmethod
    def generate_random_string():
        import random
        import string
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))

if __name__ == "__main__":
    unittest.main()