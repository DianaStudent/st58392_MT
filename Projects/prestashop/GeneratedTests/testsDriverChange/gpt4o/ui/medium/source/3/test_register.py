import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class RegistrationPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/registration")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_present_and_functional(self):
        driver = self.driver

        # Check if header elements are present and visible
        header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
        self.assertTrue(header.is_displayed(), "Header is not displayed")

        # Check for navigation links
        nav_links = {
            'home': "http://localhost:8080/en/",
            'clothes': "http://localhost:8080/en/3-clothes",
            'accessories': "http://localhost:8080/en/6-accessories",
            'art': "http://localhost:8080/en/9-art"
        }
        for name, url in nav_links.items():
            link = self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//a[@href='{url}']")))
            self.assertTrue(link.is_displayed(), f"Navigation link for {name} is not displayed")

        # Check login link
        login_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2Fregistration']")))
        self.assertTrue(login_link.is_displayed(), "Login link is not displayed")

        # Check registration form fields
        form_fields = [
            (By.ID, 'field-firstname'),
            (By.ID, 'field-lastname'),
            (By.ID, 'field-email'),
            (By.ID, 'field-password'),
            (By.ID, 'field-birthday')
        ]
        for by, value in form_fields:
            element = self.wait.until(EC.visibility_of_element_located((by, value)))
            self.assertTrue(element.is_displayed(), f"Form field {value} is not displayed")

        # Check buttons
        save_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@data-link-action='save-customer']")))
        self.assertTrue(save_button.is_displayed(), "Save button is not displayed")

        # Interact with one element (password show/hide)
        show_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@data-action='show-password']")))
        show_button.click()
        # Normally, further checks would assert visual update, but for demo, just confirm no error
        save_button.click()
        self.assertFalse(EC.alert_is_present()(driver), "Unexpected alert present after interacting")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()