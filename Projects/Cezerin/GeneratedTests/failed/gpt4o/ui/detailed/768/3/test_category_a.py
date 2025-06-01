from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestCategoryA(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.base_url = "http://localhost:3000"
        self.driver.get(self.base_url + "/category-a")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements_visibility(self):
        driver = self.driver
        wait = self.wait

        # Check Header
        header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
        self.assertTrue(header.is_displayed(), "Header is not visible")

        # Check Footer
        footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "footer")))
        self.assertTrue(footer.is_displayed(), "Footer is not visible")

        # Check Navigation Links
        for category in ["Category A", "Category B", "Category C"]:
            nav_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, category)))
            self.assertTrue(nav_link.is_displayed(), f"Navigation link for {category} is not visible")

        # Check Search Box
        search_box = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-input")))
        self.assertTrue(search_box.is_displayed(), "Search input is not visible")

        # Check Sort Dropdown
        sort_dropdown = wait.until(EC.visibility_of_element_located((By.XPATH, "//select[@value='stock_status,price,position']")))
        self.assertTrue(sort_dropdown.is_displayed(), "Sort dropdown is not visible")

        # Check Product List
        products = driver.find_elements(By.CLASS_NAME, "product-caption")
        self.assertTrue(len(products) > 0, "Products are not visible")

        # Interact with UI Elements
        if len(products) > 0:
            product = products[0]
            product.click()

            # Confirm product page load by checking URL change or any element presence
            product_name = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product-name")))
            self.assertTrue(product_name.is_displayed(), "Product page did not load properly")

        # Check Price Filter
        slider = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "rc-slider")))
        self.assertTrue(slider.is_displayed(), "Price slider is not visible")

    # More checks and interactions can be added based on requirements

if __name__ == "__main__":
    unittest.main()