import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestShopUI(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_shop_ui(self):
        # Open the page.
        self.driver.get('http://localhost/')

        # Wait for and confirm presence of key interface elements.
        expected_elements = [
            ('.nav-link', By.CSS_SELECTOR, "Home"),
            ('#input-search', By.ID, ""),
            ('button[type="submit"]', By.XPATH, ""),
            ('.alert-success', By.CSS_SELECTOR, "")
        ]
        for selector, by, value in expected_elements:
            element = WebDriverWait(self.driver, 20).until(
                EC.text_to_be_present_in_element((by, selector), value)
            )
            if not element:
                self.fail(f"Element {selector} with text '{value}' is missing")

        # Interact with one or two elements.
        button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@type='submit']")
        ))
        button.click()

        # Verify that interactive elements do not cause errors in the UI.
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-success"))
        )

if __name__ == '__main__':
    unittest.main()