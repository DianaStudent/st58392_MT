import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestEcommerceWebsite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_page_elements(self):
        # Check main UI components are present
        self._check_element_present(By.XPATH, '//h1')
        self._check_element_present(By.XPATH, '//a[@class="home"]')
        self._check_element_present(By.ID, 'search_query_top')

        # Check banners exist and are visible
        self._check_element_visible(By.XPATH, '//div[@class="header_logo"]/img')

    def test_interactive_elements(self):
        # Click button and check UI updates visually
        button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'button_search')))
        button.click()
        self._check_element_visible(By.XPATH, '//div[@class="breadcrumb"]')
        self._check_element_visible(By.XPATH, '//table[@class="product_list"]')

    def tearDown(self):
        self.driver.quit()

    def _check_element_present(self, locator_type, locator_value):
        element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((locator_type, locator_value)))
        if element is None:
            raise AssertionError(f'Element not present: {locator_type} - {locator_value}')

    def _check_element_visible(self, locator_type, locator_value):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((locator_type, locator_value)))
        if element.is_displayed() is False:
            raise AssertionError(f'Element not visible: {locator_type} - {locator_value}')

if __name__ == '__main__':
    unittest.main()