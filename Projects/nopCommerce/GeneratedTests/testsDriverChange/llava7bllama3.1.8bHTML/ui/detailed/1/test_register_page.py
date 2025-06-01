import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestMaxWebsite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_max_website_structure(self):
        # Load the page and navigate to it
        self.driver.get("http://max/")

        # Check that structural elements are visible (header, footer, navigation)
        header = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.header")))
        self.assertTrue(header.is_displayed())

        footer = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.footer")))
        self.assertTrue(footer.is_displayed())

        navigation = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "nav.navigation")))
        self.assertTrue(navigation.is_displayed())

        # Check the presence and visibility of input fields
        email_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#newsletter-email")))
        self.assertTrue(email_input.is_displayed())

        subscribe_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#newsletter-subscribe-button")))
        self.assertTrue(subscribe_button.is_displayed())

        # Check the presence and visibility of labels
        email_label = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "label[for='newsletter-email']")))
        self.assertTrue(email_label.is_displayed())

        subscribe_label = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#newsletter-subscribe-block label[for='newsletter-subscribe-button']")))
        self.assertTrue(subscribe_label.is_displayed())

        # Interact with key UI elements (click buttons)
        subscribe_button.click()

        # Confirm that the UI reacts visually
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#subscribe-loading-progress")))

        # Assert that no required UI element is missing
        self.failUnless(header.is_displayed())
        self.failUnless(footer.is_displayed())
        self.failUnless(navigation.is_displayed())
        self.failUnless(email_input.is_displayed())
        self.failUnless(subscribe_button.is_displayed())
        self.failUnless(email_label.is_displayed())
        self.failUnless(subscribe_label.is_displayed())

if __name__ == "__main__":
    unittest.main()