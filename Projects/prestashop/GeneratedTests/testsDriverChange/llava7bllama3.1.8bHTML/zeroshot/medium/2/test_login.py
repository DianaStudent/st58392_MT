import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.service import Service as ChromeService


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_login(self):
        # Open the home page.
        self.driver.get("http://localhost:8080/en/")

        # Click on the login link in the top menu.
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/login']"))).click()

        # Wait for the login page to load.
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "email")))

        # Fill in the email and password fields.
        self.driver.find_element(By.NAME, "email").send_keys("test@user.com")
        self.driver.find_element(By.NAME, "password").send_keys("test@user1")

        # Submit the login form.
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

        # Wait for page to load
        time.sleep(2)

        # Verify that login was successful by checking for the presence of "Sign out" in the top bar.
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/logout'][contains(text(), 'Sign out')]")))

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()