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
        self.driver.get("http://localhost:8080")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@data-name='Account']")))
        self.driver.find_element(By.XPATH, "//a[@data-name='Account']").click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Register']")))
        self.driver.find_element(By.XPATH, "//button[text()='Register']").click()

    def test_registration(self):
        # Wait for registration page to load
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@data-name='email']")))

        # Fill in all fields
        email = f"test_{self.random_string(10)}@user.com"
        self.driver.find_element(By.XPATH, "//input[@data-name='email']").send_keys(email)
        password = "test11"
        self.driver.find_element(By.XPATH, "//input[@data-name='password']").send_keys(password)
        repeat_password = "test11"
        self.driver.find_element(By.XPATH, "//input[@data-name='repeat-password']").send_keys(repeat_password)
        first_name = "Test"
        self.driver.find_element(By.XPATH, "//input[@data-name='first-name']").send_keys(first_name)
        last_name = "User"
        self.driver.find_element(By.XPATH, "//input[@data-name='last-name']").send_keys(last_name)

        # Select a country from the dropdown
        countries = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//ul[@class='country-list']/li")))
        countries[0].click()

        # Wait for region/state dropdown to load
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//select[@data-name='region']")))

        # Select a state only after selecting country and click on some place, to avoid country selector hide state selector.
        regions = self.driver.find_elements(By.XPATH, "//ul[@class='region-list']/li")
        regions[0].click()

        # Submit the form
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Continue']")))
        self.driver.find_element(By.XPATH, "//button[text()='Continue']").click()

    def tearDown(self):
        self.driver.quit()

    @staticmethod
    def random_string(length):
        import random
        return ''.join(random.choice('0123456789') for _ in range(length))

if __name__ == '__main__':
    unittest.main()