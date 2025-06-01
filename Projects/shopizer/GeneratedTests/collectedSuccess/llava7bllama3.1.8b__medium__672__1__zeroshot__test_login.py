from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def test_login(self):
        # Click account icon and login link
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='account-icon']"))).click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()

        # Fill in email and password fields
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "email"))).send_keys("test2@user.com")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("test**11")

        # Submit login form
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # Confirm success by checking URL and login message
        WebDriverWait(self.driver, 20).until(EC.url_contains("/my-account"))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h2[text()='My Account']")))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()