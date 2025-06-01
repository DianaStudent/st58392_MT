from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestShopizerHomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements_presence(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check that navigation links are present
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//nav//a[text()='Home']")))
            tables_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//nav//a[text()='Tables']")))
            chairs_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//nav//a[text()='Chairs']")))
        except:
            self.fail("Navigation links are not present or visible.")

        # Check that key buttons are present
        try:
            accept_cookies_btn = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            login_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/login']")))
            register_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/register']")))
        except:
            self.fail("Key buttons are not present or visible.")

        # Interact with the accept cookies button
        try:
            accept_cookies_btn.click()
        except:
            self.fail("Failed to click the Accept Cookies button.")

        # Verify that no errors occur upon interaction
        # (Additional verification can be added based on visible changes or lack of errors in the UI)

if __name__ == "__main__":
    unittest.main()