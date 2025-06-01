import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestHomePage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/")

    def tearDown(self):
        self.driver.quit()

    def test_home_page_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check Header Links
        for link_text in ["Register", "Log in", "Wishlist", "Shopping cart"]:
            element = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
            self.assertTrue(element.is_displayed(), f"{link_text} link is not displayed.")

        # Check Search Box
        search_box = wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
        self.assertTrue(search_box.is_displayed(), "Search box is not displayed.")

        search_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-box-button")))
        self.assertTrue(search_button.is_displayed(), "Search button is not displayed.")

        # Check Navigation Links
        for nav_link in ["Home page", "New products", "Search", "My account", "Blog", "Contact us"]:
            element = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, nav_link)))
            self.assertTrue(element.is_displayed(), f"{nav_link} navigation link is not displayed.")

        # Check Banner
        banner = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "slider-img")))
        self.assertTrue(banner.is_displayed(), "Banner is not displayed.")

        # Interaction: Click on 'Search' and verify redirection
        search_button.click()
        current_url = driver.current_url
        self.assertTrue(current_url.startswith("http://max/search"), "Search did not redirect correctly.")

if __name__ == "__main__":
    unittest.main()