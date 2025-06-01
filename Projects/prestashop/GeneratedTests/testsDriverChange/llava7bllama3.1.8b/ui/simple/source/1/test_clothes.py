import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestECommerceProductPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/3-clothes")  # Navigate to clothes page

    def tearDown(self):
        self.driver.quit()

    def test_main_ui_components(self):
        # Check that main UI components are present
        header = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "header")))
        product_title = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1")))
        add_to_cart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to Cart']")))

        # Check that these elements exist and are visible
        self.assertTrue(header.is_displayed())
        self.assertTrue(product_title.is_displayed())
        self.assertTrue(add_to_cart_button.is_displayed())

    def test_product_info_section(self):
        product_name = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h2")))
        price = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//p[@class='price']")))
        customer_ratings = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//span[@class='rating']")))

        # Check that these elements exist and are visible
        self.assertTrue(product_name.is_displayed())
        self.assertTrue(price.is_displayed())
        self.assertTrue(customer_ratings.is_displayed())

    def test_related_products_section(self):
        related_product_titles = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//h4[@class='product-name']")))
        for title in related_product_titles:
            self.assertTrue(title.is_displayed())
        add_to_cart_buttons = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//button[@class='add-to-cart']")))
        for button in add_to_cart_buttons:
            self.assertTrue(button.is_displayed())

    def test_login_and_register_links(self):
        login_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
        register_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Register")))

        # Check that these elements exist and are visible
        self.assertTrue(login_link.is_displayed())
        self.assertTrue(register_link.is_displayed())

if __name__ == "__main__":
    unittest.main()