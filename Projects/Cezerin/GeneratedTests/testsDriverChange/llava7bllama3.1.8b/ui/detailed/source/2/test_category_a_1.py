import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUI(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost:3000')
    
    def test_ui_components(self):
        # Check presence and visibility of structural elements
        self._check_element_visibility(By.XPATH, '//header[@class="header"]')
        self._check_element_visibility(By.XPATH, '//footer[@class="footer"]')
        self._check_element_visibility(By.XPATH, '//nav[@class="navigation"]')

        # Check input fields, buttons, labels and sections on the page
        self._check_element_visibility(By.CSS_SELECTOR, 'input[name="search"]')
        self._check_element_visibility(By.CSS_SELECTOR, 'button[type="submit"]')
        self._check_element_visibility(By.XPATH, '//label[@for="checkbox"]')
        self._check_element_visibility(By.XPATH, '//div[@class="product-info"]')

        # Interact with key UI elements
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="View details"]'))).click()
        
        # Confirm that the UI reacts visually
        self._check_element_visibility(By.XPATH, '//div[@class="product-image"]')
        self._check_element_visibility(By.XPATH, '//span[@class="price"]')

        # Check that no required UI element is missing
        if not self._is_element_present(By.XPATH, '//header[@class="header"]'):
            self.fail("Header element is missing")
        
        if not self._is_element_present(By.XPATH, '//footer[@class="footer"]'):
            self.fail("Footer element is missing")

    def tearDown(self):
        self.driver.quit()

    def _check_element_visibility(self, locator_type, locator_value):
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((locator_type, locator_value)))
        except Exception as e:
            self.fail(f"Element {locator_value} is not visible: {str(e)}")

    def _is_element_present(self, locator_type, locator_value):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((locator_type, locator_value)))

if __name__ == '__main__':
    unittest.main()