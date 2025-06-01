import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class UITestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        driver = self.driver

        # Wait for header to be visible
        header = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "header.header-area"))
        )
        self.assertTrue(header.is_displayed(), "Header not visible")

        # Wait for footer to be visible
        footer = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "footer.footer-area"))
        )
        self.assertTrue(footer.is_displayed(), "Footer not visible")

        # Check presence of navigation links
        navigation_links = ["Home", "Tables", "Chairs"]
        nav_elements = driver.find_elements(By.CSS_SELECTOR, ".main-menu nav ul li a")
        nav_texts = [nav.text for nav in nav_elements]
        for link in navigation_links:
            self.assertIn(link, nav_texts, f"{link} link not present in navigation")

        # Wait for and interact with 'Accept cookies' button
        accept_cookies_btn = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
        )
        accept_cookies_btn.click()

        # Wait for and check presence of 'Shop Now' button
        shop_now_btn = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "a.btn.btn-black"))
        )
        self.assertTrue(shop_now_btn.is_displayed(), "Shop Now button not visible")

        # Check newsletter subscription input field and button
        subscribe_input = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input.email"))
        )
        subscribe_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".subscribe-form button.button"))
        )
        self.assertTrue(subscribe_input.is_displayed(), "Subscription input field not visible")
        self.assertTrue(subscribe_button.is_displayed(), "Subscription button not visible")

if __name__ == "__main__":
    unittest.main()