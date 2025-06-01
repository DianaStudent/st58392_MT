from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestSimpleLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome() # Assuming Chrome driver is available
        self.driver.get("http://localhost:8000/dk")

    def test_login(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, 'email')))
            email_input = self.driver.find_element(By.NAME, 'email')
            email_input.send_keys("user@test.com")
            
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, 'password')))
            password_input = self.driver.find_element(By.NAME, 'password')
            password_input.send_keys("testuser")
            
            remember_me_checkbox = self.driver.find_element(By.CSS_SELECTOR, '[name="rememberMe"]')
            remember_me_checkbox.click()
            
            sign_in_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
            sign_in_button.click()
            
            welcome_message = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="customer-profile-completion"]')))
            self.assertEqual(welcome_message.text, '75%')
        except Exception as e:
            print(e)
            self.fail("Failed to login")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()