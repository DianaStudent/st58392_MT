import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # Replace with your desired browser
        
    def test_login_successfully(self):
        self.driver.get(html_data["home_before_login"])
        
        login_page_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button-1.register-button"))
        )
        login_page_button.click()
        
        email_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input.email"))
        )
        password_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "label[for=\"Password\"] ~ input[type=\"password\"]"))
        )
        
        email_input.send_keys("admin@admin.com")
        password_input.send_keys("admin")
        
        login_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button-1.login-button"))
        )
        login_button.click()
        
        logout_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@class='administration']"))
        )
        
        self.assertIn("Administration", logout_button.text)
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()