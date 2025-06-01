import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestRegister(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_register(self):
        # Open the home page.
        self.driver.get("http://localhost/")

        # Click on the account button and select "Register".
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/my-account']"))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Register"))).click()

        # Fill in the registration form.
        email = self.generate_email()
        self.driver.find_element(By.NAME, "email").send_keys(email)
        self.driver.find_element(By.NAME, "password").send_keys("test**11")
        self.driver.find_element(By.NAME, "first_name").send_keys("Test")
        self.driver.find_element(By.NAME, "last_name").send_keys("User")

        # Select a country and a region/state.
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='country_id']"))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Canada"))).click()

        # Submit the registration form.
        self.driver.find_element(By.NAME, "register").click()

        # Wait for redirect and confirm success by checking if the current URL includes "/my-account".
        WebDriverWait(self.driver, 20).until(EC.url_contains("/my-account"))

    def generate_email(self):
        return f"test{len(unittest.TestCase.__subclasses__())}@shopizer.com"

if __name__ == "__main__":
    unittest.main()