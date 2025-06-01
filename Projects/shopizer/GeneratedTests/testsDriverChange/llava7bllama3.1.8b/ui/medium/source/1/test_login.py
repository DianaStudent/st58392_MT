import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from unittest import TestCase
from selenium.webdriver.chrome.service import Service as ChromeService


class TestUIElements(TestCase):

    def setUp(self):
        os.environ['WDM_LOG_LEVEL'] = '0'  # Suppress unnecessary warnings
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost/')

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        # Confirm the presence of key interface elements: navigation links, inputs, buttons, banners.
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'nav > ul'))
        )
        
        nav_links = self.driver.find_elements(By.TAG_NAME, 'a')
        for link in nav_links:
            if not link.text in ['Dashboard', 'Products', 'Orders', 'Customers', 'Settings']:
                self.fail('Unexpected navigation link: {}'.format(link.text))
        
        # Confirm that interactive elements do not cause errors in the UI.
        try:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button'))
            ).click()
        except TimeoutException:
            self.fail('Button click caused a timeout error')
        except NoSuchElementException:
            self.fail('No button found to interact with')

    def test_element_interaction(self):
        # Interact with one or two elements — e.g., click a button and check that the UI updates visually.
        try:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button'))
            ).click()
            
            # Visual check to ensure something has changed on the page
            visual_change_element = self.driver.find_element(By.XPATH, '//div[@class="react-toast-notifications__container css-1oqa81j"]')
        except TimeoutException:
            self.fail('Button click caused a timeout error')
        except NoSuchElementException:
            self.fail('No button found to interact with')

if __name__ == '__main__':
    unittest.main()