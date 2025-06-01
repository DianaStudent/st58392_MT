import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

class TestRegistrationPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/registration")
        self.driver.maximize_window()

    def test_ui_elements_visibility(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header visibility
        header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        self.assertIsNotNone(header, "Header is not visible.")

        # Check footer visibility
        footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        self.assertIsNotNone(footer, "Footer is not visible.")

        # Check presence and visibility of form fields and buttons
        fields_and_buttons = [
            ("field-id_gender-1", "Mr. radio button"),
            ("field-id_gender-2", "Mrs. radio button"),
            ("field-firstname", "First name input"),
            ("field-lastname", "Last name input"),
            ("field-email", "Email input"),
            ("field-password", "Password input"),
            ("field-psgdpr", "Terms and conditions checkbox"),
            ("field-customer_privacy", "Customer privacy checkbox"),
            ("form-footer", "Save button"),
        ]

        for (field_id, name) in fields_and_buttons:
            element = wait.until(EC.visibility_of_element_located((By.ID, field_id)))
            self.assertIsNotNone(element, f"{name} is not visible.")

        # Interact with a button
        save_button = driver.find_element(By.CSS_SELECTOR, "button[data-link-action='save-customer']")
        ActionChains(driver).move_to_element(save_button).perform()
        self.assertIsNotNone(save_button, "Save button is not present.")

        # Check breadcrumbs
        breadcrumbs = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "breadcrumb")))
        self.assertIsNotNone(breadcrumbs, "Breadcrumbs are not visible.")
        
        # Interact - click sign in link
        sign_in_link = wait.until(EC.visibility_of_element_located(
            (By.LINK_TEXT, "Log in to your customer account")
        ))
        self.assertIsNotNone(sign_in_link, "Sign in link is not visible.")
        sign_in_link.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()