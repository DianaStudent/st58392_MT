import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPageUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/login")

    def test_UI_elements_presence_and_visibility(self):
        driver = self.driver

        elements = {
            'email': (By.ID, "field-email"),
            'password': (By.ID, "field-password"),
            'sign_in_button': (By.ID, "submit-login"),
            'forgot_password': (By.XPATH, "//a[text()='Forgot your password?']"),
            'no_account': (By.XPATH, "//a[@data-link-action='display-register-form']"),
            'language_dropdown': (By.ID, "language-selector-label"),
            'sign_in_link': (By.XPATH, "//a[@title='Log in to your customer account']"),
            'cart': (By.XPATH, "//div[@class='blockcart cart-preview inactive']")
        }

        for element_name, selector in elements.items():
            try:
                WebDriverWait(driver, 20).until(EC.visibility_of_element_located(selector))
            except:
                self.fail(f"{element_name} is not visible on the page.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()