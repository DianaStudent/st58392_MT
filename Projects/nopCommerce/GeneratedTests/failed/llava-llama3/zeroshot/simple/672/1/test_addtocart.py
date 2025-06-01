from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import ChromeDriverService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class TestMaxWebpage(unittest.TestCase):
    def setUp(self):
        driver_service = ChromeDriverService()
        options = Options()
        self.driver = webdriver.Chrome(service=driver_service, chrome_options=options)

    def tearDown(self):
        self.driver.quit()

    def test_search_and_add_to_cart(self):
        self.driver.get('http://max/')

        # Locate search box
        search_box = WebDriverWait(self.driver, 20).until(
            EC.element_located((By.XPATH, "//input[contains(@name,\"q\")]"))
        )

        # Perform search and submit
        search_box.send_keys("Max")
        self.driver.find_element_by_name('q').submit()

        # Locate success notification
        success_notification = WebDriverWait(self.driver, 20).until(
            EC.element_located((By.XPATH, "//div[contains(@class,\"success\")]"))
        )
        
        # Click on the link in the success notification to view the cart
        self.driver.find_element_by_xpath("//a[contains(@class,\"view-cart-link\")]).click()
        
        # Confirm that the shopping cart contains at least one item
        cart = WebDriverWait(self.driver, 20).until(
            EC.element_located((By.XPATH, "//div[contains(@id,\"shopping-cart\")]"))
        )
        self.assertEqual(len(cart.find_elements_by_css_selector("ul>li")), 1)
        
    def test_add_to_cart(self):
        # Locate the "Add to cart" button
        add_button = WebDriverWait(self.driver, 20).until(
            EC.element_located((By.XPATH, "//button[contains(@class,\"action-buttons-button\")]"))
        )
        
        # Click on the button to add an item to the cart
        self.driver.find_element_by_css_selector("span[role='group'][data-value='1']").click()