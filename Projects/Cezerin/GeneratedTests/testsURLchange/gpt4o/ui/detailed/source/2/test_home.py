import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000")
        self.wait = WebDriverWait(self.driver, 20)

    def test_elements_visible_and_clickable(self):
        driver = self.driver

        # Verify header is visible
        header = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        self.assertTrue(header.is_displayed(), "Header is not visible")

        # Verify navigation links
        nav_links = ["Category A", "Category B", "Category C"]
        for link_text in nav_links:
            link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
            self.assertTrue(link.is_displayed(), f"Navigation link '{link_text}' is not visible")

        # Verify search input
        search_box = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-input')))
        self.assertTrue(search_box.is_displayed(), "Search box is not visible")

        # Verify cart button
        cart_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'cart-button')))
        self.assertTrue(cart_button.is_displayed(), "Cart button is not visible")

        # Verify main slider image
        main_slider_image = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'image-gallery-image')))
        self.assertTrue(main_slider_image.is_displayed(), "Main slider image is not visible")

        # Verify 'BEST SELLERS' section
        best_sellers_title = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[text()='BEST SELLERS']")))
        self.assertTrue(best_sellers_title.is_displayed(), "'BEST SELLERS' section is not visible")

        # Verify footer is visible
        footer = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
        self.assertTrue(footer.is_displayed(), "Footer is not visible")

        # Interaction: Click 'Category A' link
        category_a_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Category A')))
        ActionChains(driver).move_to_element(category_a_link).click(category_a_link).perform()

        # Verify we are on the 'Category A' page
        self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Subcategory 1')))
        self.assertIn("category-a", driver.current_url, "Not on Category A page")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()