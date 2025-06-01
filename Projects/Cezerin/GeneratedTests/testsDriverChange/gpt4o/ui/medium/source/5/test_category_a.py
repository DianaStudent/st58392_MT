import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestCategoryAPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")

    def test_ui_elements_presence_and_interaction(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check for header elements.
        try:
            logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".logo-image img")))
            search_icon = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".icon-search img")))
            cart_icon = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart-button img")))
        except:
            self.fail("Essential header elements are missing.")

        # Check for category navigation.
        try:
            category_a_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Category A")))
            category_b_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Category B")))
            category_c_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Category C")))
        except:
            self.fail("Navigation links are not present.")

        # Check for search box.
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-input")))
        except:
            self.fail("Search input is missing.")

        # Check for product list.
        try:
            product_a = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'product-name') and text()='Product A']")))
            product_b = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'product-name') and text()='Product B']")))
        except:
            self.fail("Products are not visible.")

        # Check for filtering options.
        try:
            filter_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".button.is-fullwidth")))
            filter_button.click()
        except:
            self.fail("Filter button is not functional.")

        # Make sure interaction doesn't cause error.
        try:
            wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".error-message")))
        except:
            self.fail("Interaction caused UI error.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()