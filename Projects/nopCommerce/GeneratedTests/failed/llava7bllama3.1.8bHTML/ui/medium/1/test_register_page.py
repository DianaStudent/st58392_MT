from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class TestPage(unittest.TestCase):

    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://max/')

    def tearDown(self):
        self.driver.quit()

    def test_page_elements(self):
        try:
            # Navigation links
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/"]')))
            self.failUnless(WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/"]'))))
            
            # Inputs and buttons
            self.failUnless(WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, 'email'))))
            self.failUnless(WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#newsletter-subscribe-button'))))

            # Banners
            self.failUnless(WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//h2[contains(text(), "Newsletter")]'))))
            
            # Click a button to verify UI updates visually
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#newsletter-subscribe-button'))).click()
            self.failUnless(WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//div[@id="newsletter-result-block"]'))))
        except TimeoutException:
            self.fail('Timed out waiting for page elements')
        except NoSuchElementException as e:
            self.fail(f'Failed to locate element: {e}')

if __name__ == '__main__':
    unittest.main()