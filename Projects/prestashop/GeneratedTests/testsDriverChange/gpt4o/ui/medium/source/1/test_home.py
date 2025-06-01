import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestDemoWebsite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check for navigation links
        nav_links = [
            "http://localhost:8080/en/3-clothes",
            "http://localhost:8080/en/6-accessories",
            "http://localhost:8080/en/9-art",
            "http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art",
            "http://localhost:8080/en/registration"
        ]
        
        for link in nav_links:
            try:
                nav_element = wait.until(EC.visibility_of_element_located((By.XPATH, f"//a[@href='{link}']")))
                self.assertTrue(nav_element.is_displayed(), f"Navigation link {link} is not visible")
            except:
                self.fail(f"Navigation link {link} is not found or not visible")

        # Check for search input field
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='s']")))
            self.assertTrue(search_input.is_displayed(), "Search input field is not visible")
        except:
            self.fail("Search input field is not found or not visible")

        # Check for the carousel banner
        try:
            carousel = wait.until(EC.visibility_of_element_located((By.ID, "carousel")))
            self.assertTrue(carousel.is_displayed(), "Carousel banner is not visible")
        except:
            self.fail("Carousel banner is not found or not visible")

        # Interact with the "Sign in" button
        try:
            sign_in_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@title='Log in to your customer account']")))
            self.assertTrue(sign_in_button.is_displayed(), "Sign in button is not visible")
            sign_in_button.click()

            # Verify that the URL changes as expected upon clicking "Sign in"
            wait.until(EC.url_contains("/en/login"))
        except:
            self.fail("Sign in button interaction failed")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()