import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestSelenium(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('http://localhost:3000')

    def tearDown(self):
        self.driver.quit()

    def test_structure_and_visibility(self):
        # Header
        header = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//header')))
        self.assertTrue(header.is_displayed())

        # Footer
        footer = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//footer')))
        self.assertTrue(footer.is_displayed())

        # Navigation
        navigation = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//nav')))
        self.assertTrue(navigation.is_displayed())

        # Input Fields and Buttons
        input_fields_and_buttons = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'input, button')))
        for field_or_button in input_fields_and_buttons:
            self.assertTrue(field_or_button.is_enabled())
            self.assertTrue(field_or_button.is_displayed())

        # Section (Shopping Cart)
        shopping_cart = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="cart"]')))
        self.assertTrue(shopping_cart.is_displayed())

    def test_interaction_and_ui_reaction(self):
        # Interact with 'Empty Cart' button
        empty_cart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="empty-cart"]')))
        empty_cart_button.click()

        # Confirm UI reacts visually (e.g., cart becomes empty)
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located((By.XPATH, '//div[@class="cart"]'))))

if __name__ == "__main__":
    unittest.main()