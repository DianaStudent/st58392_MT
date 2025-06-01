import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestShopReact(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_shop_react(self):
        # Check structural elements
        header = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'header')))
        footer = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'footer')))

        # Check navigation and links
        nav_links = self.driver.find_elements(By.CSS_SELECTOR, '.nav-link')
        for link in nav_links:
            link.click()
            WebDriverWait(self.driver, 10).until(EC.url_contains(link.text))

        # Check input fields, buttons, labels, and sections
        login_form = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[id="login-form"]')))
        register_form = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form[id="register-form"]')))

        # Interact with key UI elements
        login_button = self.driver.find_element(By.CSS_SELECTOR, '.btn-primary')
        login_button.click()
        WebDriverWait(self.driver, 10).until(EC.url_contains('login'))

        # Confirm that the UI reacts visually
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h2')))

        # Assert that no required UI element is missing
        self.failUnless(header.is_displayed())
        self.failUnless(footer.is_displayed())
        self.failUnless(nav_links[0].is_displayed())

if __name__ == "__main__":
    unittest.main()