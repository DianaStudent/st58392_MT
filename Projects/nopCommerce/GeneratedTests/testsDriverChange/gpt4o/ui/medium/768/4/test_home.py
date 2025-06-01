import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestWebsiteUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_ui_elements_present_and_interactive(self):
        driver = self.driver
        driver.get("http://max/")

        # Wait and check header logo
        header_logo = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".header-logo img"))
        )
        self.assertTrue(header_logo.is_displayed(), "Header logo is not visible.")

        # Navigation links
        nav_links_text = ["Home page", "New products", "Search", "My account", "Blog", "Contact us"]
        for link_text in nav_links_text:
            link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, link_text))
            )
            self.assertTrue(link.is_displayed(), f"Navigation link '{link_text}' is not visible.")

        # Check registration and login
        reg_link = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".ico-register"))
        )
        self.assertTrue(reg_link.is_displayed(), "Register link is not visible.")

        login_link = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".ico-login"))
        )
        self.assertTrue(login_link.is_displayed(), "Login link is not visible.")

        # Check search box and button
        search_box = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-box-text"))
        )
        self.assertTrue(search_box.is_displayed(), "Search box is not visible.")

        search_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-box-button"))
        )
        self.assertTrue(search_button.is_displayed(), "Search button is not visible.")

        # Check welcome banner
        welcome_banner = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".swiper-slide-active .slider-img"))
        )
        self.assertTrue(welcome_banner.is_displayed(), "Welcome banner is not visible.")

        # Interact with the search button
        search_box.send_keys("test")
        search_button.click()
        
        # Ensure no errors and the search results or message appear
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".page-body"))
            )
        except:
            self.fail("UI did not update as expected after interacting with the search button.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()