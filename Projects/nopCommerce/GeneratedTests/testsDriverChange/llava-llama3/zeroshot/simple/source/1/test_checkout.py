import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.elemen import ElementFinder
from selenium.webdriver.support.ui import Select

class CheckoutTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_checkout(self):
        # Step 1: Search for a product and add it to cart
        driver = self.driver
        driver.get("http://max/")
        search_box = ElementFinder(driver.find_element_by_name('search'))
        search_box.send_keys('book')
        search_button = ElementFinder(driver.find_element_by_name('search-button'))
        search_button.click()
        time.sleep(2)
        cart_button = ElementFinder(driver.find_element_by_name('cart-button'))
        cart_button.click()

        # Step 2: Click shopping cart
        cart_popup = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//[id^='shopping-cart-pop-']/div[contains(text(), 'Success!')]")))
        cart_popup.click()

        # Step 3: Use the "Checkout as Guest" option
        guest_checkout_button = ElementFinder(driver.find_element_by_name('guest-checkout-button'))
        guest_checkout_button.click()
        
        # Step 4: Confirm success by checking for an order completion message
        order_completion_message = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//[id^='order-completion-message-pop-']/div[contains(text(), 'Completed')]")))
        self.assertTrue(order_completion_message)

if __name__ == '__main__':
    unittest.main()