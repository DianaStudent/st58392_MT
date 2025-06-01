import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestClothesPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/3-clothes")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Verify structural elements (header, footer, navigation)
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
            footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
            navigation = wait.until(EC.visibility_of_element_located((By.ID, "_desktop_top_menu")))

            # Check the presence of input fields, buttons, labels, sections
            search_widget = wait.until(EC.visibility_of_element_located((By.ID, "search_widget")))
            cart = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping-cart")))
            sign_in = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))

            # Verify the presence of product list section
            product_list = wait.until(EC.visibility_of_element_located((By.ID, "products")))

            # Interact with key UI elements, e.g., click buttons
            cart_button = driver.find_element(By.CLASS_NAME, "shopping-cart")
            cart_button.click()

            # Confirm that the UI reacts visually (e.g., dropdown menu, modals)
            dropdown_visible = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "cart-preview")))

        except Exception as e:
            self.fail(f"UI element verification failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()