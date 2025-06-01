from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class UITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_UI_elements(self):
        driver = self.driver

        # Check header elements
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-area")))
        except:
            self.fail("Header is not visible.")

        # Check footer elements
        try:
            footer = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer-area")))
        except:
            self.fail("Footer is not visible.")

        # Check presence of navigation links
        try:
            home_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            tables_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            chairs_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
        except:
            self.fail("One or more navigation links are not visible.")

        # Check presence of input fields and buttons
        try:
            search_field = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='email']")))
            subscribe_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Subscribe']")))
        except:
            self.fail("Search field or subscribe button is not visible.")

        # Check presence of product elements
        try:
            product = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'product-wrap')]")))
        except:
            self.fail("Product elements are not visible.")

        # Interact with buttons
        try:
            cookie_accept_button = self.wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            cookie_accept_button.click()
        except:
            self.fail("Unable to click the cookie accept button.")

        # Confirm that the UI reacts visually (verify button disappearance)
        try:
            self.wait.until(EC.invisibility_of_element((By.ID, "rcc-confirm-button")))
        except:
            self.fail("Cookie accept button did not disappear after clicking.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()