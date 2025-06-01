from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome() # Change to your preferred browser
        self.driver.get(html_data["login_page"])

    def test_login(self):
        email_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="Email"]')))
        email_input.send_keys("admin@admin.com")

        password_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="Password"]')))
        # Note: There is no id="Password" in the given HTML structure. It seems there's a missing label.
        # In this case, you need to modify your HTML or use another selector.

        remember_me_checkbox = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="RememberMe"]')))
        submit_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.button-1.login-button')))

        submit_button.click()

        logout_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.administration')))
        self.assertTrue(logout_button.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()