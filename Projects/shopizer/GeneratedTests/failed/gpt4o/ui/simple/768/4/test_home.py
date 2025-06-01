from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_main_ui_elements(self):
        driver = self.driver

        # Check the presence and visibility of header logo
        try:
            logo = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".logo img")))
            self.assertTrue(logo.is_displayed(), "Logo is not visible.")
        except:
            self.fail("Logo is not present.")

        # Check the presence and visibility of navigation links
        try:
            nav_links = ["Home", "Tables", "Chairs"]
            for link_text in nav_links:
                link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
                self.assertTrue(link.is_displayed(), f"Navigation link '{link_text}' is not visible.")
        except:
            self.fail("One or more navigation links are not present.")

        # Check the presence and visibility of the 'Accept cookies' button
        try:
            accept_cookies_button = self.wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            self.assertTrue(accept_cookies_button.is_displayed(), "Accept cookies button is not visible.")
        except:
            self.fail("Accept cookies button is not present.")

        # Check the presence and visibility of the 'Shop Now' button
        try:
            shop_now_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-black")))
            self.assertTrue(shop_now_button.is_displayed(), "Shop Now button is not visible.")
        except:
            self.fail("Shop Now button is not present.")

        # Check the presence and visibility of product images
        try:
            product_images = self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".product-img img")))
            self.assertGreater(len(product_images), 0, "Product images are not visible.")
        except:
            self.fail("Product images are not present.")

        # Check the presence and visibility of the newsletter subscription field
        try:
            subscribe_field = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".subscribe-form-3 .email")))
            self.assertTrue(subscribe_field.is_displayed(), "Newsletter subscription field is not visible.")
        except:
            self.fail("Newsletter subscription field is not present.")

        # Check the presence and visibility of the 'Subscribe' button
        try:
            subscribe_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".subscribe-form-3 .button")))
            self.assertTrue(subscribe_button.is_displayed(), "Subscribe button is not visible.")
        except:
            self.fail("Subscribe button is not present.")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()