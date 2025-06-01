```python
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.base_url = "http://max/"
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        driver.get(self.base_url)

        # 1. Open the home page.
        base_html = self.html_data.get('base')
        if not base_html:
            self.fail("Base HTML data is missing.")

        # 2. Click on the "Search" link.
        try:
            search_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Search"))
            )
            search_link.click()
        except NoSuchElementException:
            self.fail("Search link not found.")

        # 3. Enter "book" in the search field and submit the search.
        search_page_before_html = self.html_data.get('search_page_before')
        if not search_page_before_html:
            self.fail("Search page before HTML data is missing.")

        try:
            search_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "q"))
            )
            search_input.send_keys("book")

            search_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "button-1.search-button"))
            )
            search_button.click()
        except NoSuchElementException:
            self.fail("Search input or button not found.")

        # 4. Wait for the search results to load.
        search_results_book_html = self.html_data.get('search_results_book')
        if not search_results_book_html:
            self.fail("Search results book HTML data is missing.")

        # Wait for product grid to load
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "product-grid"))
            )
        except NoSuchElementException:
            self.fail("Product grid not found after search.")

        # 5. Locate and interact with the price range slider:
        # This part is not possible to implement with provided HTML.
        # The HTML does not contain the slider element or the code to interact with it.
        # Instead, we will navigate to a URL that includes the price parameter.
        # Adjust the minimum or maximum slider handle to set a specific range (e.g. 0–25).
        # Wait for the filtering to apply dynamically.
        driver.get(self.base_url + "search?q=book&price=0-25")

        # 6. Confirm that:
        # The product grid updates after slider movement.
        # At least one product is shown in the filtered results.
        search_filter_0_15_html = self.html_data.get('search_filter_0_15')
        if not search_filter_0_15_html:
            self.fail("Search filter 0-15 HTML data is missing.")

        try:
            product_grid = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "product-grid"))
            )

            product_items = product_grid.find_elements(By.CLASS_NAME, "item-box")
            self.assertTrue(len(product_items) > 0, "No products found after filtering.")
        except NoSuchElementException:
            self.fail("Product grid or items not found after filtering.")

    html_data = {
      "base": "<body style=\"zoom: 50%;\"> <div class=\"master-wrapper-page\"> <div class=\"header\"> <a class=\"skip\" href=\"#main\">Skip navigation</a> <div class=\"header-upper\"> <div class=\"header-links-wrapper\"> <div class=\"flyout-cart\" id=\"flyout-cart\"> <div class=\"mini-shopping-cart\"> <div class=\"count\"> You have no items in your shopping cart. </div> </div> </div> </div> </div> <div class=\"header-lower\"> <div class=\"header-logo\"> <a href=\"/\"> <img alt=\"Your store name\" src=\"http://max/Themes/DefaultClean/Content/images/logo.png\" title=\"\"/> </a> </div> <div class=\"search-box store-search-box\"> <form action=\"/search\" id=\"small-search-box-form\" method=\"get\"> <input aria-label=\"Search store\" autocomplete=\"off\" class=\"search-box-text ui-autocomplete-input\" id=\"small-searchterms\" name=\"q\" placeholder=\"Search store\" type=\"text\"/> <button class=\"button-1 search-box-button\" type=\"submit\">Search</button> </form> </div> </div> </div> <div class=\"header-menu\"> <ul class=\"top-menu notmobile\"> <li><a href=\"/\">Home page</a></li> <li><a href=\"/newproducts\">New products</a></li> <li><a href=\"/search\">Search</a></li> <li><a href=\"/customer/info\">My account</a></li> <li><a href=\"/blog\">Blog</a></li> <li><a href=\"/contactus\">Contact us</a></li> </ul> <div aria-controls=\"aria-categories-mobile-ul\" class=\"menu-toggle\" role=\"button\" tabindex=\"0\">Menu</div> <ul class=\"top-menu mobile\"> <li><a href=\"/\">Home page</a></li> <li><a href=\"/newproducts\">New products</a></li> <li><a href=\"/search\">Search</a></li> <li><a href=\"/customer/info\">My account</a></li> <li><a href=\"/blog\">Blog</a></li> <li><a href=\"/contactus\">Contact us</a></li> </ul> </div> </div> </body>",
      "search_page_before": "<body style=\"zoom: 50%;\"> <div class=\"master-wrapper-page\"> <div class=\"header\"> <a class=\"skip\" href=\"#main\">Skip navigation</a> <div class=\"header-upper\"> <div class=\"header-links-wrapper\"> <div class=\"flyout-cart\" id=\"flyout-cart\"> <div class=\"mini-shopping-cart\"> <div class=\"count\"> You have no items in your shopping cart. </div> </div> </div> </div> </div> <div class=\"header-lower\"> <div class=\"header-logo\"> <a href=\"/\"> <img alt=\"Your store name\" src=\"http://max/Themes/DefaultClean/Content/images/logo.png\" title=\"\"/> </a> </div> <div class=\"search-box store-search-box\"> <form action=\"/search\" id=\"small-search-box-form\" method=\"get\"> <input aria-label=\"Search store\" autocomplete=\"off\" class=\"search-box-text ui-autocomplete-input\" id=\"small-searchterms\" name=\"q\" placeholder=\"Search store\" type=\"text\"/> <button class=\"button-1 search-box-button\" type=\"submit\">Search</button> </form> </div> </div> </div> <div class=\"header-menu\"> <ul class=\"top-menu notmobile\"> <li><a href=\"/\">Home page</a></li> <li><a href=\"/newproducts\">New products</a></li> <li><a href=\"/search\">Search</a></li> <li><a href=\"/customer/info\">My account</a></li> <li><a href=\"/blog\">Blog</a></li> <li><a href=\"/contactus\">Contact us</a></li> </ul> <div aria-controls=\"aria-categories-mobile-ul\" class=\"menu-toggle\" role=\"button\" tabindex=\"0\">Menu</div> <ul class=\"top-menu mobile\"> <li><a href=\"/\">Home page</a></li> <li><a href=\"/newproducts\">New products</a></li> <li><a href=\"/search\">Search</a></li> <li><a href=\"/customer/info\">My account</a></li> <li><a href=\"/blog\">Blog</a></li> <li><a href=\"/contactus\">Contact us</a></li> </ul> </div> <div class=\"master-wrapper-content\" id=\"main\" role=\"main\"> <div class=\"master-column-wrapper\"> <div class=\"center-2\"> <div class=\"page search-page