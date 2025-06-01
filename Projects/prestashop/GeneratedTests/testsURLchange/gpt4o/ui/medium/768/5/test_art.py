import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ArtPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/9-art")
        self.wait = WebDriverWait(self.driver, 20)

    def test_page_elements(self):
        driver = self.driver
        
        # Verify navigation links
        nav_links = [
            "http://localhost:8080/en/3-clothes",
            "http://localhost:8080/en/6-accessories",
            "http://localhost:8080/en/9-art"
        ]
        for link in nav_links:
            element = self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//a[@href='{link}']")))
            self.assertIsNotNone(element, f"Navigation link for {link} is not visible")

        # Verify Login and Register links
        login_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@title='Log in to your customer account']")))
        self.assertIsNotNone(login_link, "Login link is not visible")

        register_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/registration']")))
        self.assertIsNotNone(register_link, "Register link is not visible")

        # Verify search input
        search_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='s']")))
        self.assertIsNotNone(search_input, "Search input is not visible")

        # Verify product section presence
        product_section = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//section[@id='products']")))
        self.assertIsNotNone(product_section, "Products section is not visible")

        # Verify category heading
        category_heading = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Art']")))
        self.assertIsNotNone(category_heading, "Category heading 'Art' is not visible")

        # Click 'Quick View' button of the first product and verify quick view appears
        quick_view_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@class='quick-view js-quick-view'])[1]")))
        self.assertIsNotNone(quick_view_button, "Quick view button is not visible")
        quick_view_button.click()

        # Verify Quick view modal
        quick_view_modal = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='wishlist-modal modal fade show']")))
        self.assertIsNotNone(quick_view_modal, "Quick view modal is not visible after clicking Quick view button")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()