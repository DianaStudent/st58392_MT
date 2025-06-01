from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestShopReactApp(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_key_elements_present(self):
        # Confirm the presence of key interface elements
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//nav")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//header")))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))

    def test_button_click_update_ui(self):
        # Click a button and check that the UI updates visually
        button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Add to Cart')]")))
        button.click()

        # Verify that interactive elements do not cause errors in the UI
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='react-toast-notifications__container']")))

    def test_missing_elements(self):
        # Test if any required element is missing and fail the test
        self.assertIn("nav", self.driver.find_elements(By.TAG_NAME, "nav").text)
        self.assertIn("header", self.driver.find_elements(By.TAG_NAME, "header").text)
        self.assertIn("Search", self.driver.find_elements(By.XPATH, "//input[@placeholder='Search']").get_attribute('value'))

if __name__ == "__main__":
    unittest.main()