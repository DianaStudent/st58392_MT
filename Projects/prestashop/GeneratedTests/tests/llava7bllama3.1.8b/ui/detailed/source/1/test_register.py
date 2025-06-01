import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestRegistrationPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://localhost:8080/en/registration')

    def test_registration_page(self):
        # Check structural elements
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'header')))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'footer')))

        # Check input fields and labels
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, 'name')))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, 'email')))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, 'password')))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, 'confirm_password')))

        # Check buttons and links
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]')))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//a[text()="Login"]')))

        # Interact with key UI elements
        submit_button = self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()

        # Confirm that the UI reacts visually
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//div[@class="alert alert-success"]')))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()