import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestHomepageUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/")

    def test_ui_elements_present(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Check header elements
        header_links = wait.until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.header-links a'))
        )
        self.assertTrue(all(link.is_displayed() for link in header_links), "Not all header links are visible")

        # Check for Search Box
        search_box = wait.until(
            EC.visibility_of_element_located((By.ID, 'small-search-box-form'))
        )
        self.assertTrue(search_box.is_displayed(), "Search box is not visible")

        # Check for Register and Login link
        register_link = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.ico-register'))
        )
        self.assertTrue(register_link.is_displayed(), "Register link is not visible")

        login_link = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.ico-login'))
        )
        self.assertTrue(login_link.is_displayed(), "Login link is not visible")

        # Check for Main Home Page Links
        top_menu_links = wait.until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.top-menu.notmobile a'))
        )
        self.assertTrue(all(link.is_displayed() for link in top_menu_links), "Not all top menu links are visible")

        # Check for Wishlist and Cart
        wishlist_link = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.ico-wishlist'))
        )
        self.assertTrue(wishlist_link.is_displayed(), "Wishlist link is not visible")

        cart_link = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.ico-cart'))
        )
        self.assertTrue(cart_link.is_displayed(), "Cart link is not visible")

        # Check for Footer Links
        footer_links = wait.until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.footer-block .list li a'))
        )
        self.assertTrue(all(link.is_displayed() for link in footer_links), "Not all footer links are visible")

        # Check for Newsletter Subscription
        newsletter_input = wait.until(
            EC.visibility_of_element_located((By.ID, 'newsletter-email'))
        )
        self.assertTrue(newsletter_input.is_displayed(), "Newsletter input is not visible")

        newsletter_button = wait.until(
            EC.visibility_of_element_located((By.ID, 'newsletter-subscribe-button'))
        )
        self.assertTrue(newsletter_button.is_displayed(), "Newsletter subscribe button is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()