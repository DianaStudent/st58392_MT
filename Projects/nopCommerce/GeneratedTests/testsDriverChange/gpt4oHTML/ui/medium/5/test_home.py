import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestHomePageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_verify_ui_elements(self):
        driver = self.driver

        # Check presence of header links
        try:
            register_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
            login_link = driver.find_element(By.LINK_TEXT, "Log in")
            wishlist_link = driver.find_element(By.CSS_SELECTOR, ".ico-wishlist")
            cart_link = driver.find_element(By.CSS_SELECTOR, ".ico-cart")
        except:
            self.fail("One or more key header links are missing.")

        # Check presence of search box and button
        try:
            search_box = driver.find_element(By.ID, "small-searchterms")
            search_button = driver.find_element(By.CSS_SELECTOR, ".search-box-button")
        except:
            self.fail("Search box or button is missing.")

        # Check presence of banners
        try:
            banners = driver.find_elements(By.CSS_SELECTOR, ".slider-img")
            self.assertGreater(len(banners), 0, "Banners are missing on the homepage.")
        except:
            self.fail("Banners check failed on the homepage.")

        # Interact with search and check UI updates
        search_box.send_keys("Test product")
        search_button.click()

        # Verify search results page by checking navigation to search URL
        try:
            self.wait.until(EC.url_contains("/search"))
        except:
            self.fail("Search interaction did not update the UI or navigate correctly.")

        # Ensure interactive elements do not cause UI errors
        try:
            driver.find_element(By.ID, "bar-notification")
        except:
            self.fail("Error in UI - Notification bar missing or causing issues.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()