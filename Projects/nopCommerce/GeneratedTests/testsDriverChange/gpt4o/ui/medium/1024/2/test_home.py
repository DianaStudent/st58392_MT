import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

class TestHomePage(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("--headless")  # Run headlessly if desired
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("http://max/")

    def test_ui_elements(self):
        driver = self.driver

        # Verify navigation links
        nav_links = [
            (By.LINK_TEXT, "Home page"),
            (By.LINK_TEXT, "New products"),
            (By.LINK_TEXT, "Search"),
            (By.LINK_TEXT, "My account"),
            (By.LINK_TEXT, "Blog"),
            (By.LINK_TEXT, "Contact us")
        ]

        for link_text in nav_links:
            element = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located(link_text),
                f"Navigation link {link_text[1]} not found or not visible"
            )

        # Verify header-logo is present and visible
        header_logo = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "header-logo")),
            "Header logo not visible"
        )

        # Verify search box is present and visible
        search_box = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "small-searchterms")),
            "Search box not visible"
        )

        # Verify main banner (swiper) is present and visible
        main_banner = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "nop-slider")),
            "Main banner not visible"
        )

        # Click and interact with an element
        search_box.clear()
        search_box.send_keys("test")
        search_button = driver.find_element(By.CSS_SELECTOR, "button.search-box-button")
        search_button.click()

        # Verify the search execution doesn't cause errors
        WebDriverWait(driver, 20).until(EC.url_contains("/search?"), "Search functionality did not work properly")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()