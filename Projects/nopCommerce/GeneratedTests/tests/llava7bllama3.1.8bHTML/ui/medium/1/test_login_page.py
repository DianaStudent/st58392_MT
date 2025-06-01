import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestMaxWebsite(unittest.TestCase):

    def setUp(self):
        os.environ['WDM_LOCAL'] = '1'
        self.driver = webdriver.Chrome()
        self.driver.get('http://max/')

    def test_main_page_elements(self):
        # Navigation links
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="ui-helper-hidden-accessible"]//following-sibling::nav[1]')))
        navigation_links = self.driver.find_elements(By.XPATH, '//div[@class="ui-helper-hidden-accessible"]//following-sibling::nav[1]/a')
        self.assertEqual(len(navigation_links), 2)

        # Inputs
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//input[@type="email" and @name="newsletter-email"]')))
        email_input = self.driver.find_element(By.XPATH, '//input[@type="email" and @name="newsletter-email"]')
        self.assertEqual(email_input.get_attribute('type'), 'email')

        # Buttons
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//button[@id="newsletter-subscribe-button"]')))
        subscribe_button = self.driver.find_element(By.XPATH, '//button[@id="newsletter-subscribe-button"]')
        self.assertEqual(subscribe_button.get_attribute('id'), 'newsletter-subscribe-button')

        # Banners
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="block title"]')))
        banners = self.driver.find_elements(By.XPATH, '//div[@class="block title"]')
        self.assertEqual(len(banners), 2)

    def test_subscribe_button_click(self):
        # Click subscribe button
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//button[@id="newsletter-subscribe-button"]')))
        subscribe_button = self.driver.find_element(By.XPATH, '//button[@id="newsletter-subscribe-button"]')
        subscribe_button.click()

        # Check UI updates visually (not implemented in this example)

    def test_interactive_elements(self):
        # Click subscribe button
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//button[@id="newsletter-subscribe-button"]')))
        subscribe_button = self.driver.find_element(By.XPATH, '//button[@id="newsletter-subscribe-button"]')
        subscribe_button.click()

        # Check no errors in UI (not implemented in this example)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()