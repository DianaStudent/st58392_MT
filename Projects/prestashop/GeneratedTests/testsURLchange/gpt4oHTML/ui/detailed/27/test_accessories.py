import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestAccessoriesPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/en/6-accessories")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_ui_components(self):
        driver = self.driver

        # Check for header
        header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
        self.assertTrue(header.is_displayed(), "Header is not visible")

        # Check for footer
        footer = driver.find_element(By.ID, "footer")
        self.assertTrue(footer.is_displayed(), "Footer is not visible")

        # Check for navigation menu
        top_menu = driver.find_element(By.ID, "top-menu")
        self.assertTrue(top_menu.is_displayed(), "Top menu is not visible")

        # Check for contact link
        contact_link = driver.find_element(By.ID, "_desktop_contact_link")
        self.assertTrue(contact_link.is_displayed(), "Contact link is not visible")

        # Check for language selector
        language_selector = driver.find_element(By.ID, "_desktop_language_selector")
        self.assertTrue(language_selector.is_displayed(), "Language selector is not visible")

        # Check for user info (Sign in)
        user_info = driver.find_element(By.ID, "_desktop_user_info")
        self.assertTrue(user_info.is_displayed(), "User info is not visible")

        # Check for cart
        cart = driver.find_element(By.ID, "_desktop_cart")
        self.assertTrue(cart.is_displayed(), "Cart is not visible")

        # Check for search widget
        search_widget = driver.find_element(By.ID, "search_widget")
        self.assertTrue(search_widget.is_displayed(), "Search widget is not visible")

        # Interact with header elements
        home_link = driver.find_element(By.CSS_SELECTOR, "a[href='http://localhost:8080/en/']")
        self.assertTrue(home_link.is_displayed(), "Home link is not visible")
        home_link.click()

        # Wait for homepage to load and check its visibility
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body#category")))

        # Check for subcategories
        subcategories = driver.find_element(By.ID, "subcategories")
        self.assertTrue(subcategories.is_displayed(), "Subcategories are not visible")

        # Check for products list
        product_list = driver.find_element(By.ID, "js-product-list")
        self.assertTrue(product_list.is_displayed(), "Product list is not visible")

        # Check for product count
        product_count = driver.find_element(By.CSS_SELECTOR, "div.total-products p")
        self.assertTrue(product_count.is_displayed(), "Product count is not visible")

        # Check for newsletter subscription input
        newsletter_input = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
        self.assertTrue(newsletter_input.is_displayed(), "Newsletter input is not visible")

        # Check for subscribe button
        subscribe_button = driver.find_element(By.NAME, "submitNewsletter")
        self.assertTrue(subscribe_button.is_displayed(), "Subscribe button is not visible")

        # Assert if any required element is missing
        missing_elements = [element for element in driver.find_elements(By.CSS_SELECTOR, 'input, button, label, section, h1') if not element.is_displayed()]
        if missing_elements:
            self.fail(f"The following elements are not visible: {missing_elements}")

        # Confirm that interactions lead to visual reactions
        subscribe_button.click()
        self.wait.until(EC.alert_is_present(), "Subscribe button click did not trigger visual reaction")

if __name__ == "__main__":
    unittest.main()