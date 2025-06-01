import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/registration")

    def test_ui_elements_presence_and_visibility(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check structural elements visibility
        self._check_element_presence_and_visibility(wait, By.ID, "header")
        self._check_element_presence_and_visibility(wait, By.ID, "footer")
        self._check_element_presence_and_visibility(wait, By.ID, "main")
        
        # Check form elements and buttons
        self._check_element_presence_and_visibility(wait, By.ID, "field-firstname")
        self._check_element_presence_and_visibility(wait, By.ID, "field-lastname")
        self._check_element_presence_and_visibility(wait, By.ID, "field-email")
        self._check_element_presence_and_visibility(wait, By.ID, "field-password")
        self._check_element_presence_and_visibility(wait, By.CSS_SELECTOR, "button[type='submit']")

        # Interact with key UI Elements
        self._check_element_presence_and_visibility(wait, By.LINK_TEXT, "Log in instead!")
        self._check_element_presence_and_visibility(wait, By.LINK_TEXT, "Contact us")
        self._check_element_presence_and_visibility(wait, By.LINK_TEXT, "Clothes")
        self._check_element_presence_and_visibility(wait, By.LINK_TEXT, "Accessories")
        self._check_element_presence_and_visibility(wait, By.LINK_TEXT, "Art")

        # UI Interaction
        register_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
        register_button.click()

        # Confirm UI response (though in this mock test we don't expect any new page to load without submission)
        form_feedback = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.page-content.card.card-block"), "Create an account"))

    def _check_element_presence_and_visibility(self, wait, by, locator):
        try:
            element = wait.until(EC.presence_of_element_located((by, locator)))
            self.assertTrue(element.is_displayed(), f"Element located by {by} with locator '{locator}' is not visible.")
        except:
            self.fail(f"Element located by {by} with locator '{locator}' is missing or not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()