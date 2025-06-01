import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class ArtPageUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/9-art")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_present_and_visible(self):
        driver = self.driver
        wait = self.wait

        # Check if header is present and visible
        header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
        if not header:
            self.fail("Header not found or not visible")

        # Check if the logo is present
        logo = driver.find_element(By.CSS_SELECTOR, "#_desktop_logo img")
        if not logo.is_displayed():
            self.fail("Logo not visible")

        # Check if the menu links are present and visible
        menu_links = [
            driver.find_element(By.CSS_SELECTOR, '#top-menu > li > a[href="http://localhost:8080/en/9-art"]'),
            driver.find_element(By.CSS_SELECTOR, '#top-menu > li > a[href="http://localhost:8080/en/3-clothes"]'),
            driver.find_element(By.CSS_SELECTOR, '#top-menu > li > a[href="http://localhost:8080/en/6-accessories"]')
        ]
        for link in menu_links:
            if not link.is_displayed():
                self.fail(f"Menu link {link.get_attribute('href')} not visible")

        # Check if language selector exists and visible
        lang_selector = driver.find_element(By.CSS_SELECTOR, "#_desktop_language_selector")
        if not lang_selector.is_displayed():
            self.fail("Language selector not visible")

        # Check if the search bar is present and visible
        search_input = driver.find_element(By.CSS_SELECTOR, "#search_widget input[type='text']")
        if not search_input.is_displayed():
            self.fail("Search bar not visible")

        # Check if the login link is present and visible
        login_link = driver.find_element(By.CSS_SELECTOR, 'a[title="Log in to your customer account"]')
        if not login_link.is_displayed():
            self.fail("Login link not visible")

        # Check if product list exists and visible
        product_list = driver.find_element(By.ID, "js-product-list")
        if not product_list.is_displayed():
            self.fail("Product list not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()