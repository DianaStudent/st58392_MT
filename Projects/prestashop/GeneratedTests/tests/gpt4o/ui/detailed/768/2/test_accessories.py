import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class AccessoriesPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/6-accessories")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Verify presence of header, footer, and main sections
        self.verify_presence(By.ID, "header", "Header not found.")
        self.verify_presence(By.ID, "footer", "Footer not found.")
        self.verify_presence(By.ID, "wrapper", "Main section not found.")

        # Verify presence and visibility of navigation links
        self.verify_presence(By.LINK_TEXT, "Home", "Home link not found.")
        self.verify_presence(By.LINK_TEXT, "Clothes", "Clothes link not found.")
        self.verify_presence(By.LINK_TEXT, "Accessories", "Accessories link not found.")
        self.verify_presence(By.LINK_TEXT, "Art", "Art link not found.")

        # Verify presence of search input
        self.verify_presence(By.NAME, "s", "Search input not found.")

        # Verify presence and visibility of sign in button
        self.verify_presence(By.XPATH, "//a[@title='Log in to your customer account']", "Sign in button not found.")

        # Interact with key elements
        self.interact_with_element(By.NAME, "s", "Search input not active.")
        self.interact_with_element(By.XPATH, "//a[@title='Log in to your customer account']", "Sign in button not clickable.")

        # Check for any missing elements
        self.assert_elements()

    def verify_presence(self, by, value, error_message):
        try:
            element = self.wait.until(EC.visibility_of_element_located((by, value)))
            self.assertTrue(element.is_displayed(), error_message)
        except:
            self.fail(error_message)

    def interact_with_element(self, by, value, error_message):
        try:
            element = self.wait.until(EC.element_to_be_clickable((by, value)))
            element.click()
        except:
            self.fail(error_message)

    def assert_elements(self):
        required_elements = ["header", "footer", "wrapper"]
        for elem in required_elements:
            self.verify_presence(By.ID, elem, f"{elem.capitalize()} is missing.")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()