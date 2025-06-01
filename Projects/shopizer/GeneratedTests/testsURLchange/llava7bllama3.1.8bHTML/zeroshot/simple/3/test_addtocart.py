from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager

class TestCartFunctionality(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_cart_functionality(self):
        # Open the webpage
        self.driver.get('http://localhost/')

        # Find product item and hover over it to reveal "Add to cart" button
        product_item_xpath = "//table[@class='table table-bordered']//tr[1]/td"
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, product_item_xpath)))
        self.driver.find_element(By.XPATH, product_item_xpath).find_element_by_css_selector('.btn-group').click()

        # Open cart popup by clicking the cart icon
        cart_icon_xpath = "//i[@class='fas fa-shopping-cart']"
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, cart_icon_xpath)))
        self.driver.find_element(By.XPATH, cart_icon_xpath).click()

        # Confirm success by checking that the popup contains at least one item
        cart_popup_xpath = "//div[@class='modal-content']//table"
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, cart_popup_xpath)))
        self.assertTrue(len(self.driver.find_elements(By.XPATH, cart_popup_xpath)) > 0)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()