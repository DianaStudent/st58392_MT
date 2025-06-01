from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class LoginPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/login?returnUrl=%2F")

    def test_login_page_elements(self):
        # Check presence and visibility of input fields, buttons, labels, and sections
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "username")))
        username_field = self.driver.find_element(By.ID, "username")
        self.assertTrue(username_field.is_displayed())

        password_field = self.driver.find_element(By.ID, "password")
        self.assertTrue(password_field.is_displayed())

        login_button = self.driver.find_element(By.ID, "login-button")
        self.assertTrue(login_button.is_displayed())

        forget_password_link = self.driver.find_element(By.LINK_TEXT, "Forget Password")
        self.assertTrue(forget_password_link.is_displayed())

        sign_up_link = self.driver.find_element(By.LINK_TEXT, "Sign Up")
        self.assertTrue(sign_up_link.is_displayed())

    def test_login_button_click(self):
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()
        # Wait for the UI to react visually (e.g., loading animation)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='loading-animation']")))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()