import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.select import Select
from selenium.webdriver.common.text_fields import TextFields
from selenium.webdriver.common.file_upload import FileUpload

class TestSuite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()
    
    def test_order_place(self):
        # Step 1: Open home page.
        self.assertTrue(EC.visibility_of_element_located((By.XPATH, ''))