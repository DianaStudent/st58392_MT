import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class TestProcess(unittest.TestCase):
    def setUp(self):
        opts = Options()
        opts.headless = True
        self.driver = webdriver.Chrome(options=opts)

    def tearDown(self):
        self.driver.quit()

    def test_process(self):
        # Home page
        self.assertEqual(self.driver.title, 'Home')

        # Clothes
        self.wait_for_element_by_id('clothes')
        for i in range(1, 10):
            name = f'Clothes {i}'
            self.wait_for_element_by_name(name)
            text = self.wait_for_element_by_name(f'Text {i}')
            self.assertEqual(text.get_attribute('value'), name)

        # Accessories
        self.wait_for_element_by_id('accessories')
        for i in range(1, 10):
            name = f'Accessories {i}'
            self.wait_for_element_by_name(name)
            text = self.wait_for_element_by_name(f'Text {i}')
            self.assertEqual(text.get_attribute('value'), name)

        # Art
        self.wait_for_element_by_id('art')
        for i in range(1, 10):
            name = f'Art {i}'
            self.wait_for_element_by_name(name)
            text = self.wait_for_element_by_name(f'Text {i}')
            self.assertEqual(text.get_attribute('value'), name)

        # Login
        self.wait_for_element_by_id('login')
        username_field = self.wait_for_element_by_name('username')
        password_field = self.wait_for_element_by_name('password')
        login_button = self.wait_for_element_by_name('login')
        self.assertTrue(username_field.get_attribute('placeholder') == 'Username')

    def wait_for_element(self, by_type, by_id):
        WebDriverWait(self.driver, 20).until(
            lambda x: self.driver.find_elements(by_type, by_id)
        )

if __name__ == '__main__':
    unittest.main()