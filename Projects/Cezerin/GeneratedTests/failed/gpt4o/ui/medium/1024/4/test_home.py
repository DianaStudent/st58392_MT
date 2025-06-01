from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check presence of navigation links
        try:
            nav_link_a = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/category-a"]')))
            nav_link_b = driver.find_element(By.CSS_SELECTOR, 'a[href="/category-b"]')
            nav_link_c = driver.find_element(By.CSS_SELECTOR, 'a[href="/category-c"]')
        except Exception as e:
            self.fail(f"Navigation links are not present or visible: {e}")

        # Check presence of search input
        try:
            search_input = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.search-input')))
        except Exception as e:
            self.fail(f"Search input is not present or visible: {e}")

        # Check presence of search icon
        try:
            search_icon = driver.find_element(By.CSS_SELECTOR, 'img.search-icon-search')
        except Exception as e:
            self.fail(f"Search icon is not present or visible: {e}")

        # Check presence of cart button
        try:
            cart_button = driver.find_element(By.CSS_SELECTOR, 'span.cart-button')
        except Exception as e:
            self.fail(f"Cart button is not present or visible: {e}")

        # Check banner presence
        try:
            banner_image = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'img[src="/assets/images/slide8.jpg"]')))
        except Exception as e:
            self.fail(f"Banner image is not present or visible: {e}")

        # Interacting with an element and checking UI update
        try:
            nav_link_a.click()
            self.wait.until(EC.url_to_be("http://localhost:3000/category-a"))
            subcategory_link = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/category-a-1"]')))
            subcategory_link.click()
            self.wait.until(EC.url_to_be("http://localhost:3000/category-a-1"))
        except Exception as e:
            self.fail(f"Interactions with nav links failed or did not update UI as expected: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()