import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check header
        try:
            header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
        except:
            self.fail("Header is not visible.")

        # Check footer
        try:
            footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))
        except:
            self.fail("Footer is not visible.")

        # Check navigation links
        navigation_links = ["Home page", "New products", "Search", "My account", "Blog", "Contact us"]
        for link_text in navigation_links:
            try:
                link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
            except:
                self.fail(f"Navigation link '{link_text}' is not visible.")

        # Check search box
        try:
            search_box = wait.until(EC.visibility_of_element_located((By.ID, "small-search-box-form")))
        except:
            self.fail("Search box is not visible.")

        # Check search button
        try:
            search_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-box-button")))
        except:
            self.fail("Search button is not visible.")

        # Check slider presence
        try:
            slider = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "swiper-wrapper")))
        except:
            self.fail("Slider is not visible.")
        
        # Check newsletter subscription
        try:
            newsletter_input = wait.until(EC.visibility_of_element_located((By.ID, "newsletter-email")))
            newsletter_button = wait.until(EC.visibility_of_element_located((By.ID, "newsletter-subscribe-button")))
        except:
            self.fail("Newsletter subscription elements are not visible.")

        # Interact with search box
        search_box.find_element(By.ID, "small-searchterms").send_keys("test")
        search_button.click()

        # Confirm UI reaction (ensure results page loads)
        try:
            WebDriverWait(driver, 10).until(EC.url_contains("/search"))
        except:
            self.fail("Search did not redirect to the search results page.")
        
        # Check cart visibility and actions (flyout)
        try:
            cart_link = wait.until(EC.visibility_of_element_located((By.ID, "topcartlink")))
            cart_link.click()
            flyout_cart = wait.until(EC.visibility_of_element_located((By.ID, "flyout-cart")))
        except:
            self.fail("Cart or flyout cart is not visible or interactable.")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()