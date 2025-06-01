import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestShopReactApp(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def test_shop_react_app(self):
        # Step 1: Load the page and ensure that structural elements are visible.
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.TAG_NAME, "footer")))

        # Step 2: Check the presence and visibility of input fields, buttons, labels, and sections.
        self._check_visibility(By.ID, "name")
        self._check_visibility(By.ID, "description")
        self._check_visibility(By.CSS_SELECTOR, "#new-product-button")

        # Step 3: Interact with key UI elements (e.g., click buttons).
        new_product_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#new-product-button")))
        new_product_button.click()

        # Step 4: Confirm that the UI reacts visually.
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "product-name")))

    def _check_visibility(self, locator_type, value):
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((locator_type, value)))
        except TimeoutException:
            self.fail(f"Element {value} is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()