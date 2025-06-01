from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager

class TestRegistrationPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_registration_page(self):
        # Navigate to the registration page
        self.driver.get("http://localhost/register")

        # Verify presence of header title and icon
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1[text()='register']")))
        register_icon = self.driver.find_element(By.XPATH, "//img[@alt='register-icon']")
        self.assertTrue(register_icon.is_displayed())

        # Verify presence of logo and navigation links
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "(//a[@href='/'])[1]")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//nav//ul/li/a")))

        # Verify presence of form fields
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "firstName")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "lastName")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "emailAddress")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "password")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "repeatPassword")))

        # Verify presence of submit button
        submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        self.assertTrue(submit_button.is_displayed())

        # Verify backdrop image is visible
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.background-image")))
        background_image = self.driver.find_element(By.CSS_SELECTOR, "div.background-image")
        self.assertTrue(background_image.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()