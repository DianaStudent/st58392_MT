from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService

class TestMaxPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_max_page(self):
        # Open the page.
        self.driver.get("http://max/")

        # Confirm the presence of key interface elements
        self.assertIn("nav", self.driver.page_source)
        self.assertIn("input", self.driver.page_source)
        self.assertIn("button", self.driver.page_source)
        self.assertIn("banner", self.driver.page_source)

        # Interact with one or two elements (e.g., click a button and check that the UI updates visually).
        try:
            button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button")))
            button.click()
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Button clicked')]")))
        except TimeoutException as e:
            self.fail("Element not found: {}".format(e))

        # Verify that interactive elements do not cause errors in the UI.
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button")))
        except TimeoutException as e:
            self.fail("Timeout error: {}".format(e))

if __name__ == "__main__":
    unittest.main()