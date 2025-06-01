from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import ChromeDriverService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.assertions import Assert

class EcommerceTest(unittest.TestCase):
    def setUp(self):
        service = ChromeDriverService executable_path='/path/to/chromedriver')
        options = Options()
        self.driver = webdriver.Chrome(service=service, options=options)

    def tearDown(self):
        self.driver.quit()

    def test_ecommerce_page(self):
        # Test scenario
        driver = self.driver

        # 1. Open the page.
        driver.get('http://localhost:8080/en/')

        # 2. Confirm the presence of key interface elements: navigation links, inputs, buttons, banners.
        assert 'Home' in driver.title
        assert driver.find_element_by_css_selector('a[href$="/en/home"]').is_displayed()

        # 3. Interact with one or two elements e.g. click a button and check that the UI updates visually.
        driver.find_element_by_css_selector('button[translate="Translate"]').click()
        WebDriverWait(self.driver, 20).until(
            lambda driver: driver.title != driver.get_title(),
            'The title of the page did not change after clicking the button'
        )

        # Verify that interactive elements do not cause errors in the UI.
        assert driver.find_element_by_css_selector('a[href$="/en/new-arrivals"]').is_displayed()

if __name__ == '__main__':
    unittest.main()