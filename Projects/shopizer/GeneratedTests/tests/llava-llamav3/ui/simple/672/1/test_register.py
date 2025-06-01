import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import Until

class TestRegistrationPage(unittest.TestCase):
    def setUp(self):
        # Set up the WebDriver using ChromeDriver.
        driver = webdriver.Chrome()
        self.driver = driver
        self.driver.implicitly_wait(20, TimeUnit.SECONDS)

    def tearDown(self):
        # Close the WebDriver when the test is finished.
        self.driver.quit()

    def test_registration_page(self):
        # Go to the registration page.
        self.driver.get('http://localhost/register')

        # Check that the main UI components are present and visible.
        self.assertEqual(self.driver.title, 'Shopify - Register')
        self.assertTrue(self.driver.find_element_by_name('name'))
        self.assertTrue(self.driver.find_element_by_name('email'))
        self.assertTrue(self.driver.find_element_by_name('phone'))

        # Select the "Sign up" option in the navigation menu.
        select = Select(self.driver.find_element_by_name('nav'))
        select.select_by_index(0)

        # Check that the "Chairs" category page is loaded.
        self.driver.get('http://localhost/category/chairs')
        self.assertEqual(self.driver.title, 'Shopify - Chairs')

if __name__ == '__main__':
    unittest.main()