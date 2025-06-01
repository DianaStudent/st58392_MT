import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class ShopizerUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def test_ui_elements_present_and_visible(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check the header
        header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header.header-area")))
        self.assertTrue(header.is_displayed(), "Header is not visible")

        # Check the footer
        footer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer.footer-area")))
        self.assertTrue(footer.is_displayed(), "Footer is not visible")

        # Check the logo
        logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.logo > a > img")))
        self.assertTrue(logo.is_displayed(), "Logo is not visible")

        # Check navigation links
        nav_links = ["Home", "Tables", "Chairs", "Login", "Register"]
        for link_text in nav_links:
            link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
            self.assertTrue(link.is_displayed(), f"{link_text} link is not visible")

        # Check "Accept cookies" button
        cookies_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
        self.assertTrue(cookies_button.is_displayed(), "Accept cookies button is not visible")

        # Interact with "Accept cookies" button
        cookies_button.click()

        # Check that the product list is visible
        product_list = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.shop-bottom-area")))
        self.assertTrue(product_list.is_displayed(), "Product list is not visible")

        # Check each product card
        product_cards = driver.find_elements(By.CSS_SELECTOR, "div.product-wrap")
        for card in product_cards:
            self.assertTrue(card.is_displayed(), "Product card is not visible")

            # Check "Add to cart" button on each product
            add_to_cart_btn = card.find_element(By.CSS_SELECTOR, "div.pro-cart > button")
            self.assertTrue(add_to_cart_btn.is_displayed(), "'Add to cart' button on a product card is not visible")
            add_to_cart_btn.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()