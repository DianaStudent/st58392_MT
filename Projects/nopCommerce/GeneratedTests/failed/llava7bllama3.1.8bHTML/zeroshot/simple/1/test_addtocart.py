from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class TestCart(unittest.TestCase):
    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://max/") # replace with your website URL

    def test_cart(self):
        search_box = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#search_query_top"))
        )
        
        search_box.send_keys("book")
        
        submit_button = self.driver.find_element(By.NAME, "submit_search")
        
        submit_button.click()
        
        success_notification = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//p[@class='alert alert-success']/a"))
        )
        
        cart_link = success_notification.get_attribute("href")
        
        self.driver.get(cart_link)
        
        cart_item_count = self.driver.find_elements(By.CSS_SELECTOR, ".cart_list .product-container").__len__()
        
        self.assertGreaterEqual(cart_item_count, 1)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()