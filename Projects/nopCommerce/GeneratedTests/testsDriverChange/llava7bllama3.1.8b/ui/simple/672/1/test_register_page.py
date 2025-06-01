import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRegistrationPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://max/register?returnUrl=%2F')

    def test_registration_page_elements(self):
        # Check that the main UI components are present
        self.assertEqual(len(self.driver.find_elements(By.TAG_NAME, 'header')), 1)
        self.assertEqual(len(self.driver.find_elements(By.TAG_NAME, 'form')), 1)

        # Check that the form fields and submit button exist and are visible
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.NAME, 'full_name'))
        )
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.NAME, 'email_address'))
        )
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.NAME, 'password'))
        )
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.NAME, 'confirm_password'))
        )
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))
        )

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()