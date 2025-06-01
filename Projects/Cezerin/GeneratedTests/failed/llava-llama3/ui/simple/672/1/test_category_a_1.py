from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class LogoUploadTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_logo_upload(self):
        driver = self.driver

        # Open the main UI page
        main_page_url = "http://localhost:3000"
        driver.get(main_page_url)

        # Check that the logo upload interface is present
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'logo-upload')))
        self.assertTrue("Your Logo" in driver.page_source)

        # Navigate to category A
        category_a_url = "http://localhost:3000/category-a"
        driver.get(category_a_url)

        # Check that the logo upload interface is present
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'logo-upload')))
        self.assertTrue("Your Logo" in driver.page_source)

        # Navigate to category A-1
        category_a_1_url = "http://localhost:3000/category-a-1"
        driver.get(category_a_1_url)

        # Check that the logo upload interface is present
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'logo-upload')))
        self.assertTrue("Your Logo" in driver.page_source)