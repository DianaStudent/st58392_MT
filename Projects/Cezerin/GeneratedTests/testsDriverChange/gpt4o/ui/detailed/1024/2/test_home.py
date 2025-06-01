import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestHomePageUI(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000")
        self.wait = WebDriverWait(self.driver, 20)

    def test_main_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check header visibility
        header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        if not header.is_displayed():
            self.fail("Header is not displayed")

        # Check footer visibility
        footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
        if not footer.is_displayed():
            self.fail("Footer is not displayed")

        # Check navigation links
        self.check_element_visible(By.LINK_TEXT, "Category A")
        self.check_element_visible(By.LINK_TEXT, "Category B")
        self.check_element_visible(By.LINK_TEXT, "Category C")

        # Check search input field
        self.check_element_visible(By.CSS_SELECTOR, "input.search-input")

        # Check cart visibility
        self.check_element_visible(By.CSS_SELECTOR, "span.cart-button img[alt='cart']")

        # Check for best sellers section
        best_sellers = self.check_element_visible(By.CSS_SELECTOR, "div.title.is-4.has-text-centered")
        if "BEST SELLERS" not in best_sellers.text:
            self.fail("Best Sellers title is not displayed correctly")

        # Check product names and prices
        self.check_element_visible(By.LINK_TEXT, "Product A")
        self.check_element_visible(By.LINK_TEXT, "Product B")

        # Verify slider interaction
        slider_bullet = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'image-gallery-bullet')))
        slider_bullet.click()
        slider_active = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'image-gallery-bullet.active')))
        if not slider_active.is_displayed():
            self.fail("Slider did not react visually")

    def check_element_visible(self, by, value):
        element = self.wait.until(EC.visibility_of_element_located((by, value)))
        if not element.is_displayed():
            self.fail(f"Element {value} is not displayed")
        return element

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()