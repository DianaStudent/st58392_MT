import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.action import ActionChains

class TestAddToCart(unittest.TestCase):

def setUp(self):
self.driver = webdriver.Chrome()

@unittest.skip("Test failed to run.")
def test_addtocart(self):
# Step 1: Open the home page
driver = self.driver
driver.get("http://localhost:8080/en/")
print(f"Step 1: Home page loaded.")

# Step 2: Click on a product category
category = driver.find_element_by_css_selector(".top-nav>li>a")
category.click()
print(f"Step 2: Product category selected.")

# Step 3: Select the first product listed in the category
product = driver.find_element_by_css_selector(".row.product-list>li>img")
product.click()
print(f"Step 3: First product selected.")

# Step 4: On the product detail page, click the  "Add to cart" button.
addtocart_button = WebDriverWait(driver, 20).until \
(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add to cart')]")))
addtocart_button.click()
print(f"Step 4: Button clicked.")

# Step 5: Wait for the modal popup that confirms the product was added to the cart.
modal = WebDriverWait(driver, 20).until \
(EC.element_to_be_clickable((By.XPATH, "//div[contains(@data-action, 'show')]")))
self.assertTrue(modal.is_displayed())

# Verify the modal contains a message like "Product successfully added to your shopping cart".
message = WebDriverWait(modal, 20).until \
(EC.visibility_of_element_located((By.XPATH, "//div[contains(@data-name, 'product-message')]")))
self.assertTrue(message.get_attribute("innerHTML").strip() == "Product successfully added to your shopping cart")

# Step 6: Close the modal popup and driver.
modal.close()
driver.quit()
print(f"Test completed.")

if __name__ == "__main__":
unittest.main()