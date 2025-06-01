import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAccessoriesPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/en/6-accessories")

    def test_ui_elements_presence_and_visibility(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check presence and visibility of header
        header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        self.assertTrue(header.is_displayed(), "Header is not visible")

        # Check presence and visibility of footer
        footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        self.assertTrue(footer.is_displayed(), "Footer is not visible")

        # Check presence and visibility of navigation
        main_navigation = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".header-nav"))
        )
        self.assertTrue(main_navigation.is_displayed(), "Main navigation is not visible")

        # Check presence and visibility of input fields, buttons, labels, and sections
        category_title = wait.until(
            EC.visibility_of_element_located((By.TAG_NAME, "h1"))
        )
        self.assertEqual(category_title.text, "Accessories")

        search_bar = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#search_widget input[type='text']"))
        )
        self.assertTrue(search_bar.is_displayed(), "Search bar is not visible")

        # Check some product elements for presence
        product_element = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".js-product"))
        )
        self.assertTrue(product_element.is_displayed(), "Product element is not visible")

        # Interact with key UI elements
        cart_button = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#_desktop_cart"))
        )
        cart_button.click()

        # Check reaction to click (no navigation or errors)
        cart_products_count = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart-products-count"))
        )
        self.assertTrue(cart_products_count.is_displayed(), "Cart products count is not visible")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()