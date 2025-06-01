from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class ShopizerUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_presence(self):
        driver = self.driver

        # Validate header elements
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/']")))
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category/tables']")))
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category/chairs']")))
        except:
            self.fail("Main navigation links are not visible.")

        # Validate the presence of login and register links
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/login']")))
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/register']")))
        except:
            self.fail("Login/Register links are not visible.")

        # Validate the presence of the input field in the subscription form
        try:
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='email']")))
        except:
            self.fail("Subscription email input is not visible.")

        # Validate the presence of the 'Accept Cookies' button
        try:
            accept_cookies_button = self.wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            self.assertTrue(accept_cookies_button.is_displayed(), "Accept cookies button is not visible.")
        except:
            self.fail("Accept cookies button is not visible.")

        # Click the 'Accept Cookies' button and ensure UI updates
        accept_cookies_button.click()
        self.assertFalse(self.element_exists(By.ID, "rcc-confirm-button"), "Accept button is still visible after click.")

    def element_exists(self, by, value):
        try:
            self.driver.find_element(by, value)
        except:
            return False
        return True

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()