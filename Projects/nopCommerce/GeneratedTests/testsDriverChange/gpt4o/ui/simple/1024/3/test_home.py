import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestHomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_elements_visible(self):
        driver = self.driver

        # Check the presence and visibility of the header links
        try:
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'ico-register')))
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'ico-login')))
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'ico-wishlist')))
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'ico-cart')))
        except Exception as e:
            self.fail(f"Header links are not visible: {e}")

        # Check the logo
        try:
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header-logo')))
        except Exception as e:
            self.fail(f"Logo is not visible: {e}")

        # Check the search box
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, 'small-search-box-form')))
        except Exception as e:
            self.fail(f"Search box is not visible: {e}")

        # Check the menu links
        top_menu_links = ['Home page', 'New products', 'Search', 'My account', 'Blog', 'Contact us']
        for link_text in top_menu_links:
            try:
                self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
            except Exception as e:
                self.fail(f"Top menu link '{link_text}' is not visible: {e}")

        # Check the footer links
        footer_links = ['Sitemap', 'Shipping & returns', 'Privacy notice', 'Conditions of Use', 'About us', 'Contact us']
        for link_text in footer_links:
            try:
                self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
            except Exception as e:
                self.fail(f"Footer link '{link_text}' is not visible: {e}")

        # Check newsletter subscription
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, 'newsletter-email')))
            self.wait.until(EC.visibility_of_element_located((By.ID, 'newsletter-subscribe-button')))
        except Exception as e:
            self.fail(f"Newsletter subscription elements are not visible: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()