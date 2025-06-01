import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestShopReact(unittest.TestCase):

    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost/')

    def test_shop_react(self):
        # Wait for header and footer to be visible
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//header'))
        )
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//footer'))
        )

        # Check presence and visibility of input fields, buttons, labels
        expected_elements = [
            ('//input[@name="username"]', 'username field'),
            ('//input[@name="password"]', 'password field'),
            ('//button[@type="submit"]', 'login button'),
            ('//a[href="/category/tables"]', 'tables link'),
            ('//a[href="/category/chairs"]', 'chairs link'),
        ]
        for selector, name in expected_elements:
            element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, selector))
            )
            self.assertEqual(element.is_displayed(), True, f'{name} is not visible')

        # Interact with key UI elements
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()