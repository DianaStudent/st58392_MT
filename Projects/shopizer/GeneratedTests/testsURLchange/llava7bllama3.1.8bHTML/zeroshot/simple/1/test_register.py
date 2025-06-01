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

    def test_registration(self):
        # Open the URL
        self.driver.get("http://localhost/")

        # Click on the "Register" button
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@variant='link']"))).click()

        # Fill all fields for registration
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "email"))).send_keys("test_email@example.com")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "password"))).send_keys("test**11")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "confirm_password"))).send_keys("test**11")

        # Submit the form
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # Confirm success by checking that the browser is redirected to a page containing "/my-account" in the URL
        url = self.driver.current_url
        self.assertIn("/my-account", url)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()