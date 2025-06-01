import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestWebApp(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost:8080/en/')

    def tearDown(self):
        self.driver.quit()

    def test_main_page(self):
        # Check navigation links
        nav_links = self.driver.find_elements(By.CSS_SELECTOR, 'nav ul li a')
        for link in nav_links:
            if not link.is_displayed():
                self.fail(f'Navigation link {link.text} is missing')

        # Check form fields
        form_fields = self.driver.find_elements(By.CSS_SELECTOR, 'form input[type="text"], form input[type="password"]')
        for field in form_fields:
            if not field.is_displayed():
                self.fail(f'Form field {field.get_attribute("name")} is missing')

        # Check buttons
        buttons = self.driver.find_elements(By.CSS_SELECTOR, 'button')
        for button in buttons:
            if not button.is_displayed():
                self.fail(f'Button {button.text} is missing')

        # Check banners
        banner = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.breadcrumb')))
        if not banner.is_displayed():
            self.fail('Banner is missing')

        # Click a button and check that the UI updates visually
        buttons[0].click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h1')))

    def test_interactive_elements(self):
        # Check interactive elements do not cause errors in the UI
        nav_links = self.driver.find_elements(By.CSS_SELECTOR, 'nav ul li a')
        for link in nav_links:
            link.click()
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.breadcrumb')))

if __name__ == '__main__':
    unittest.main(verbosity=2)