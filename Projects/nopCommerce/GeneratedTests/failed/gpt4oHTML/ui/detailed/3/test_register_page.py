from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/register?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)

    def test_page_elements(self):
        driver = self.driver

        # Check for header visibility
        header = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
        self.assertTrue(header.is_displayed(), "Header is not visible.")

        # Check for footer visibility
        footer = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))
        self.assertTrue(footer.is_displayed(), "Footer is not visible.")

        # Check for input fields and their visibility
        input_fields = [
            (By.ID, "FirstName", "First Name"),
            (By.ID, "LastName", "Last Name"),
            (By.ID, "Email", "Email"),
            (By.ID, "Password", "Password"),
            (By.ID, "ConfirmPassword", "Confirm Password"),
        ]

        for locator, field_name in input_fields:
            field = self.wait.until(EC.visibility_of_element_located(locator))
            if not field.is_displayed():
                self.fail(f"{field_name} input field is not visible.")

        # Check for Register button and click it
        register_button = self.wait.until(EC.visibility_of_element_located((By.ID, "register-button")))
        if not register_button.is_displayed():
            self.fail("Register button is not visible.")
        register_button.click()

        # Confirm UI reacts visually, assuming some reaction placeholder like notifications
        notification_area = self.wait.until(EC.visibility_of_element_located((By.ID, "bar-notification")))
        self.assertTrue(notification_area.is_displayed(), "Notification area did not react visibly.")

        # Check for labels and sections
        labels_and_sections = [
            (By.CLASS_NAME, "page-title", "Page Title"),
            (By.XPATH, "//div[@class='fieldset']/div[@class='title']", "Section Titles"),
        ]

        for locator, description in labels_and_sections:
            element = self.wait.until(EC.visibility_of_all_elements_located(locator))
            if not any(el.is_displayed() for el in element):
                self.fail(f"{description} are not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()