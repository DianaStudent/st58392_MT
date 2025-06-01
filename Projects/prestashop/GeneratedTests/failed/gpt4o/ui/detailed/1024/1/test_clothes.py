from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class ClothesPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements_visibility(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Load the page
        driver.get("http://localhost:8080/en/3-clothes")

        elements_to_check = {
            "header": (By.ID, "header"),
            "footer": (By.ID, "footer"),
            "navigation": (By.ID, "_desktop_top_menu"),
            "language_selector": (By.ID, "_desktop_language_selector"),
            "user_info": (By.ID, "_desktop_user_info"),
            "search_widget": (By.ID, "search_widget"),
            "contact_link": (By.ID, "contact-link"),
            "cart": (By.ID, "_desktop_cart"),
            "product_list": (By.CSS_SELECTOR, "#js-product-list .products"),
            "product_item": (By.CSS_SELECTOR, ".js-product.product"),
            "newsletter_input": (By.CSS_SELECTOR, "input[name='email']"),
            "subscribe_button": (By.CSS_SELECTOR, "input[name='submitNewsletter']"),
        }

        # Check presence and visibility of elements
        for name, locator in elements_to_check.items():
            try:
                element = wait.until(EC.visibility_of_element_located(locator))
                self.assertTrue(element.is_displayed(), f"{name} should be visible")
            except Exception as e:
                self.fail(f"{name} is not visible: {str(e)}")

        # Interact with a button to confirm UI changes
        filter_button = driver.find_element(By.ID, "search_filter_toggler")
        filter_button.click()
        filter_controls = wait.until(EC.visibility_of_element_located((By.ID, "search_filters")))
        self.assertTrue(filter_controls.is_displayed(), "Filter controls should become visible after clicking 'Filter'")

if __name__ == "__main__":
    unittest.main()