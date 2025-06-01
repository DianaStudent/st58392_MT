from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestUIElements(unittest.TestCase):

    def setUp(self):
        # Setup the Chrome WebDriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

    def test_ui_elements_presence_and_interaction(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check the existence of the main UI components on the page

        # Header navigation links
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            tables_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            chairs_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
        except:
            self.fail("Navigation links are not present or visible.")

        # Cookie consent button
        try:
            cookie_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
        except:
            self.fail("Cookie consent button is not present or visible.")

        # Subscribe email input and button
        try:
            email_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='email']")))
            subscribe_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.button")))
        except:
            self.fail("Subscribe input or button is not present or visible.")

        # Interacting with elements: Clicking the Cookie consent button
        cookie_button.click()

        # Check that interactive elements do not cause errors
        # We will confirm that the cookie consent div is no longer visible after click
        try:
            wait.until(EC.invisibility_of_element_located((By.ID, "rcc-confirm-button")))
        except:
            self.fail("Cookie consent button did not disappear after clicking.")

if __name__ == "__main__":
    unittest.main()