from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/search")

    def test_ui_elements(self):
        driver = self.driver

        elements = {
            "logo": (By.CSS_SELECTOR, ".header-logo img"),
            "search_input": (By.ID, "small-searchterms"),
            "search_button": (By.CSS_SELECTOR, "button.button-1.search-box-button"),
            "register_link": (By.CSS_SELECTOR, "a.ico-register"),
            "login_link": (By.CSS_SELECTOR, "a.ico-login"),
            "wishlist_link": (By.CSS_SELECTOR, "a.ico-wishlist"),
            "cart_link": (By.CSS_SELECTOR, "a.ico-cart"),
            "sort_by_dropdown": (By.ID, "products-orderby"),
            "display_dropdown": (By.ID, "products-pagesize"),
            "product_items": (By.CSS_SELECTOR, ".product-item"),
            "advanced_search_toggle": (By.ID, "advs"),
        }

        for element_name, selector in elements.items():
            try:
                WebDriverWait(driver, 20).until(EC.visibility_of_element_located(selector))
            except Exception as e:
                self.fail(f"{element_name} not found or not visible.")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()