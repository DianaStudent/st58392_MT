import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestArtPageUI(unittest.TestCase):

    def setUp(self):
        # Setup Chrome WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/9-art")
        self.wait = WebDriverWait(self.driver, 20)

    def test_art_page_elements(self):
        driver = self.driver

        try:
            # Check for header
            header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
            self.assertIsNotNone(header)

            # Check for main navigation links
            home_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            clothes_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
            accessories_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories")))
            art_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Art")))
            
            self.assertTrue(home_link.is_displayed())
            self.assertTrue(clothes_link.is_displayed())
            self.assertTrue(accessories_link.is_displayed())
            self.assertTrue(art_link.is_displayed())

            # Check for search input field
            search_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "s")))
            self.assertTrue(search_input.is_displayed())

            # Check for Sign in button
            sign_in_button = self.wait.until(EC.visibility_of_element_located((
                By.XPATH, "//a[@title='Log in to your customer account']"
            )))
            self.assertTrue(sign_in_button.is_displayed())

            # Interact with elements: click "Art" link and confirm it navigates correctly
            art_link.click()
            self.wait.until(EC.url_to_be("http://localhost:8080/en/9-art"))
            self.assertEqual(driver.current_url, "http://localhost:8080/en/9-art")

            # Check for no UI errors after interaction
            notification_area = self.wait.until(EC.visibility_of_element_located((By.ID, "notifications")))
            self.assertIsNotNone(notification_area)

        except Exception as e:
            self.fail(str(e))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()