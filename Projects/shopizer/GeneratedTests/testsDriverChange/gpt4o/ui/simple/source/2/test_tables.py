import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestWebPage(unittest.TestCase):

    def setUp(self):
        # Setup Chrome WebDriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost/")

    def test_UI_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header logo
        try:
            logo = wait.until(EC.visibility_of_element_located((
                By.CSS_SELECTOR, "div.logo > a > img"
            )))
            assert logo.is_displayed()
        except Exception:
            self.fail("Logo is not visible.")

        # Check navigation links
        try:
            home_link = wait.until(EC.visibility_of_element_located((
                By.LINK_TEXT, "Home"
            )))
            assert home_link.is_displayed()
            
            tables_link = driver.find_element(By.LINK_TEXT, "Tables")
            assert tables_link.is_displayed()
            
            chairs_link = driver.find_element(By.LINK_TEXT, "Chairs")
            assert chairs_link.is_displayed()
        except Exception:
            self.fail("Navigation links are not visible.")

        # Check the "Accept" button for cookies
        try:
            accept_button = wait.until(EC.visibility_of_element_located((
                By.ID, "rcc-confirm-button"
            )))
            assert accept_button.is_displayed()
        except Exception:
            self.fail("Cookie 'Accept' button is not visible.")

        # Check key product elements
        try:
            product_image = wait.until(EC.visibility_of_element_located((
                By.CSS_SELECTOR, "div.product-img > a > img"
            )))
            assert product_image.is_displayed()
            
            add_to_cart_button = driver.find_element(By.CSS_SELECTOR, "div.pro-cart > button")
            assert add_to_cart_button.is_displayed()
        except Exception:
            self.fail("Product elements are not visible.")

        # Check footer elements
        try:
            footer_logo = wait.until(EC.visibility_of_element_located((
                By.CSS_SELECTOR, "div.footer-logo > a > img"
            )))
            assert footer_logo.is_displayed()
        except Exception:
            self.fail("Footer logo is not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()