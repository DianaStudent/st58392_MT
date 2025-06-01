from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestHomePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_home_page(self):
        self.driver.get("http://localhost")  # Replace with your actual URL
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "header")))

        elements_to_check = [
            ("h1", "home-products-title"),
            ("button", "checkout-button button is-primary"),
            ("a", "facebook"),
            ("input", "search-input"),
            ("div", "home-products")
        ]

        for element in elements_to_check:
            try:
                WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, element[0])))
                self.assertTrue(self.driver.find_element(By.TAG_NAME, element[0]).is_displayed())
            except TimeoutException:
                self.fail(f"Missing required UI element: {element}")

        # Interact with key UI elements
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='checkout-button button is-primary']")))
        self.driver.find_element(By.XPATH, "//button[@class='checkout-button button is-primary']").click()

        # Confirm that the UI reacts visually
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "reacted-visually")))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()