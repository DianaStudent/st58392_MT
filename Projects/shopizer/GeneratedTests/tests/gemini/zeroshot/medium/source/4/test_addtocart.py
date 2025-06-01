import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver

        # Accept cookies
        try:
            cookie_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

        # Hover over the "Chair" product image to reveal the "Add to cart" button
        chair_product = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/product/chair']/img[@alt='']"))
        )
        
        actions = ActionChains(driver)
        actions.move_to_element(chair_product).perform()

        # Click the "Add to cart" button for the "Chair" product
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/product/chair']/ancestor::div[@class='product-img']/following-sibling::div[@class='product-action-2']/button[@title='Add to cart']"))
        )
        add_to_cart_button.click()

        # Hover over the "Olive Table" product image to reveal the "Add to cart" button
        olive_table_product = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/product/olive-table']/img[@alt='']"))
        )
        
        actions = ActionChains(driver)
        actions.move_to_element(olive_table_product).perform()

        # Click the "Add to cart" button for the "Olive Table" product
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/product/olive-table']/ancestor::div[@class='product-img']/following-sibling::div[@class='product-action-2']/button[@title='Add to cart']"))
        )
        add_to_cart_button.click()

        # Open the cart popup by clicking the cart icon
        cart_icon = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart"))
        )
        cart_icon.click()

        # Verify that at least one product is listed in the popup cart
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='shopping-cart-content active']/ul/li"))
            )
        except:
            self.fail("No products found in the cart popup")

if __name__ == "__main__":
    unittest.main()