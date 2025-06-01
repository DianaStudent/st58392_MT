from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestHomePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://yourdomain.com")  # replace with your domain

    def test_homepage_elements(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'header')))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.category_a')))

        self.assertTrue(self.is_element_visible(By.CSS_SELECTOR, '.category_a_1'))

    def test_homepage_interactions(self):
        button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button')))
        button.click()

    def is_element_visible(self, locator):
        try:
            element = self.driver.find_element(*locator)
            return element.is_displayed()
        except:
            return False

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()