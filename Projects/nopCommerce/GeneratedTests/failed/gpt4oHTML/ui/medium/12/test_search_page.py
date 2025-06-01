from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUiProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/search")
        self.driver.maximize_window()

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check presence of navigation links
        nav_links = {
            "Home": "/",
            "New products": "/newproducts",
            "Search": "/search",
            "My account": "/customer/info",
            "Blog": "/blog",
            "Contact us": "/contactus",
        }
        
        for link_text, link_href in nav_links.items():
            link = wait.until(EC.visibility_of_element_located((By.XPATH, f"//a[@href='{link_href}']")))
            self.assertTrue(link.is_displayed(), f"Link {link_text} not visible")

        # Check presence of the search input field
        search_input = wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
        self.assertTrue(search_input.is_displayed(), "Search input not visible")

        # Check presence of the search button
        search_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".button-1.search-box-button")))
        self.assertTrue(search_button.is_displayed(), "Search button not visible")

        # Check presence of the advanced search checkbox
        adv_search_checkbox = wait.until(EC.visibility_of_element_located((By.ID, "advs")))
        self.assertTrue(adv_search_checkbox.is_displayed(), "Advanced search checkbox not visible")

        # Interact with advanced search checkbox
        adv_search_checkbox.click()
        advanced_search_block = wait.until(EC.visibility_of_element_located((By.ID, "advanced-search-block")))
        self.assertTrue(advanced_search_block.is_displayed(), "Advanced search block not visible after clicking checkbox")

        # Check presence of one product from search results
        product_item = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-item[data-productid='1']")))
        self.assertTrue(product_item.is_displayed(), "Product item not visible in search results")

        # Interact with a product 'Add to cart' button
        add_to_cart_button = product_item.find_element(By.CSS_SELECTOR, ".button-2.product-box-add-to-cart-button")
        add_to_cart_button.click()

        # Verify AJAX loading block does not display (no errors in UI)
        ajax_loading_block = driver.find_element(By.CSS_SELECTOR, ".ajax-loading-block-window")
        is_displayed = ajax_loading_block.value_of_css_property('display') == 'none'
        self.assertTrue(is_displayed, "AJAX loading block should not be displayed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()