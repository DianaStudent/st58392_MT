import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestHomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_elements_presence(self):
        driver = self.driver

        # Verify header elements
        try:
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".header")))
        except:
            self.fail("Header not visible.")

        # Verify logo
        try:
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".header-logo img")))
        except:
            self.fail("Logo not visible.")

        # Verify search box
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
        except:
            self.fail("Search box not visible.")

        # Verify search button
        try:
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-box-button")))
        except:
            self.fail("Search button not visible.")

        # Verify top menu links
        menu_links = [
            (By.LINK_TEXT, "Home page"),
            (By.LINK_TEXT, "New products"),
            (By.LINK_TEXT, "Search"),
            (By.LINK_TEXT, "My account"),
            (By.LINK_TEXT, "Blog"),
            (By.LINK_TEXT, "Contact us")
        ]
        for index, link in enumerate(menu_links):
            try:
                self.wait.until(EC.visibility_of_element_located(link))
            except:
                self.fail(f"Menu link at index {index} not visible.")

        # Verify footer elements
        try:
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".footer")))
        except:
            self.fail("Footer not visible.")

        # Verify subscribe elements
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, "newsletter-email")))
            self.wait.until(EC.visibility_of_element_located((By.ID, "newsletter-subscribe-button")))
        except:
            self.fail("Newsletter subscribe elements not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()