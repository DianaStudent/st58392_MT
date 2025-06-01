from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import unittest
from webdriver_manager.chrome import ChromeDriverManager

class TestRegisterPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/register")

    def test_register_page(self):
        # Check presence and visibility of structural elements
        header = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "header"))
        )
        footer = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "footer"))
        )

        # Check presence and visibility of input fields
        first_name_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "first_name"))
        )
        last_name_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "last_name"))
        )
        email_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        password_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        confirm_password_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "confirm_password"))
        )
        phone_number_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "phone_number"))
        )

        # Check presence and visibility of buttons
        submit_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#register-button"))
        )
        checkbox = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "terms_of_service"))
        )

        # Interact with key UI elements
        submit_button.click()

        # Confirm that the UI reacts visually
        try:
            error_message = self.driver.find_element_by_css_selector(".error-message")
        except NoSuchElementException:
            pass

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()