import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        try:
            # Check header elements
            header = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
            self.assertTrue(header.is_displayed(), "Header is not visible.")

            # Check footer elements
            footer = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))
            self.assertTrue(footer.is_displayed(), "Footer is not visible.")

            # Check navigation links
            top_menu_links = ["Home page", "New products", "Search", "My account", "Blog", "Contact us"]
            for link_text in top_menu_links:
                nav_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
                self.assertTrue(nav_link.is_displayed(), f"{link_text} link is not visible.")

            # Check search functionality
            search_input = self.wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
            self.assertTrue(search_input.is_displayed(), "Search input is not visible.")
            search_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-box-button")))
            self.assertTrue(search_button.is_displayed(), "Search button is not visible.")

            # Interact with search input
            search_input.send_keys("book")
            search_button.click()

            # Check if search results are displayed
            search_results = self.wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "search-results"))
            )
            self.assertTrue(search_results.is_displayed(), "Search results are not visible.")

            # Check presence of login and register links
            login_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Log in")))
            self.assertTrue(login_link.is_displayed(), "Login link is not visible.")
            register_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
            self.assertTrue(register_link.is_displayed(), "Register link is not visible.")

            # Check presence of other main UI components
            price_slider = self.wait.until(
                EC.visibility_of_element_located((By.ID, "price-range-slider"))
            )
            self.assertTrue(price_slider.is_displayed(), "Price range slider is not visible.")

        except Exception as e:
            self.fail(f"UI Test failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()