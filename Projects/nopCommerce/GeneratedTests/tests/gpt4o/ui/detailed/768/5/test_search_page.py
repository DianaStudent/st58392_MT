import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/search")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements_present_and_visible(self):
        driver = self.driver
        wait = self.wait

        try:
            # Check header elements
            header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
            header_links = header.find_element(By.CLASS_NAME, "header-links")
            self.assertTrue(header_links.is_displayed(), "Header links are not visible")

            # Check navigation menu
            top_menu = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "top-menu")))
            self.assertTrue(top_menu.is_displayed(), "Top menu is not visible")

            # Check search box
            search_box = wait.until(EC.visibility_of_element_located((By.ID, "small-search-box-form")))
            search_input = search_box.find_element(By.ID, "small-searchterms")
            search_button = search_box.find_element(By.CLASS_NAME, "search-box-button")
            self.assertTrue(search_input.is_displayed() and search_button.is_displayed(), "Search input or button is not visible")

            # Check form fields
            search_keyword_field = wait.until(EC.visibility_of_element_located((By.ID, "q")))
            search_button_main = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-button")))
            self.assertTrue(search_keyword_field.is_displayed() and search_button_main.is_displayed(), "Search keyword field or button is not visible")

            # Check price filter
            price_range_slider = wait.until(EC.visibility_of_element_located((By.ID, "price-range-slider")))
            self.assertTrue(price_range_slider.is_displayed(), "Price range slider is not visible")

            # Interact with search input
            search_keyword_field.clear()
            search_keyword_field.send_keys("book")
            search_button_main.click()

            # Check that at least one product item is visible
            product_item = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product-item")))
            self.assertTrue(product_item.is_displayed(), "Product items are not visible after search")

        except Exception as e:
            self.fail(f"Test failed due to missing or non-visible element: {str(e)}")

if __name__ == "__main__":
    unittest.main()