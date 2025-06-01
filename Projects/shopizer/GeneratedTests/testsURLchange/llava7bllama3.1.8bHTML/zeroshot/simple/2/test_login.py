from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost/")

    def test_login(self):
        # Click account icon
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='account-icon']"))).click()

        # Click login link
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/my-account/login']"))).click()

        # Switch to iframe (not shown in the provided HTML)
        WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "content-frame")))

        # Fill email
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='email']"))).send_keys("test2@user.com")

        # Fill password
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']"))).send_keys("test**11")

        # Click submit button
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

        # Check that the browser is redirected to a page containing "/my-account" in the URL
        self.assertIn("/my-account", self.driver.current_url)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()