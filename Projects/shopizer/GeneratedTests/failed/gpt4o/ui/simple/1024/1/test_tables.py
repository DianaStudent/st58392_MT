from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestShopizerUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements_present(self):
        driver = self.driver

        # Check if the logo is visible
        logo = self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '.logo img')
        ))
        self.assertTrue(logo.is_displayed(), "Logo is not visible.")

        # Check if the navigation links are visible
        nav_links = ["Home", "Tables", "Chairs"]
        for link_text in nav_links:
            link = self.wait.until(EC.visibility_of_element_located(
                (By.LINK_TEXT, link_text)
            ))
            self.assertTrue(link.is_displayed(), f"{link_text} link is not visible.")

        # Check if login and register links are visible
        login_link = self.wait.until(EC.visibility_of_element_located(
            (By.LINK_TEXT, "Login")
        ))
        self.assertTrue(login_link.is_displayed(), "Login link is not visible.")

        register_link = self.wait.until(EC.visibility_of_element_located(
            (By.LINK_TEXT, "Register")
        ))
        self.assertTrue(register_link.is_displayed(), "Register link is not visible.")

        # Check if the product grid/table is visible
        product_grid = self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '.shop-area .grid.three-column')
        ))
        self.assertTrue(product_grid.is_displayed(), "Product grid is not visible.")

        # Check if each product's "Add to cart" button is visible
        add_to_cart_buttons = driver.find_elements(By.CSS_SELECTOR, '.pro-cart button')
        self.assertTrue(add_to_cart_buttons, "No 'Add to cart' buttons found.")
        for button in add_to_cart_buttons:
            self.assertTrue(button.is_displayed(), "'Add to cart' button is not visible.")

        # Check if the footer is visible
        footer = self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '.footer-area')
        ))
        self.assertTrue(footer.is_displayed(), "Footer is not visible.")

if __name__ == "__main__":
    unittest.main()