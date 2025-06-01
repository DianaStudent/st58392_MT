from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestArtPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/9-art")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_visibility(self):
        driver = self.driver

        # Check header visibility
        header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
        if not header.is_displayed():
            self.fail("Header is not visible")

        # Check footer visibility
        footer = self.wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        if not footer.is_displayed():
            self.fail("Footer is not visible")

        # Check navigation links
        nav_links = {
            "home": "http://localhost:8080/en/",
            "clothes": "http://localhost:8080/en/3-clothes",
            "accessories": "http://localhost:8080/en/6-accessories",
            "art": "http://localhost:8080/en/9-art"
        }
        for name, url in nav_links.items():
            nav_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//a[@href='{url}']")))
            if not nav_link.is_displayed():
                self.fail(f"Navigation link for {name} is not visible")

        # Check for login and register buttons
        login_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art']")))
        register_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/registration']")))

        if not login_button.is_displayed():
            self.fail("Login button is not visible")

        if not register_button.is_displayed():
            self.fail("Register button is not visible")

        # Check for search input field visibility
        search_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='text' and @name='s']")))
        if not search_input.is_displayed():
            self.fail("Search input field is not visible")

        # Interact with the search field
        search_input.send_keys("Framed posters")
        
        # Check for available products
        product_list = self.wait.until(EC.visibility_of_element_located((By.ID, "js-product-list")))
        if not product_list.is_displayed():
            self.fail("Product list is not visible")

        # Check product items' visibility
        products = driver.find_elements(By.CLASS_NAME, "js-product")
        for product in products:
            if not product.is_displayed():
                self.fail("A product is not visible")

        # Click the first product's quick view button
        quick_view_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@class='quick-view js-quick-view'])[1]")))
        quick_view_button.click()

        # Confirm that the quick view modal appears
        quick_view_modal = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "modal-content")))
        if not quick_view_modal.is_displayed():
            self.fail("Quick view modal did not appear")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()