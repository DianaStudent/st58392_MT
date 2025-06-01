import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestHomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('http://localhost:8000')

    def test_home_page(self):
        # Structural elements
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//header"))
        )
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//footer"))
        )

        # Input fields, buttons and labels
        self.assert_required_elements_present([
            ('//input[@name="search"]', 'Search field'),
            ('//button[@type="submit"]', 'Submit button'),
            ('//label[@for="remember-me"]', 'Remember me label')
        ])

    def assert_required_elements_present(self, elements):
        for element in elements:
            try:
                WebDriverWait(self.driver, 20).until(
                    EC.visibility_of_element_located((By.XPATH, element[0]))
                )
            except TimeoutException:
                self.fail(f"Element '{element[1]}' is missing")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()