from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class TestShoppingCartCompletion(unittest.TestCase):
def setUp(self):
self.driver = webdriver.Chrome()

def tearDown(self):
self.driver.quit()

def test_shopping_cart_completion(self):
# 1. Open the homepage.
driver.get("http://max/")

# 2. Navigate to the "Search" page and look for a product using the query "book".
search_box = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='search']"))))
search_box.send_keys("book")
search_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='search-button']"))))

# 3. Add the first result to the cart using a product tile button.
product_tile_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'product-tile')]//button[contains(@class,'product-tile-button')]")))
product_tile_button.click()

# 4. From the success notification, click the "shopping cart" link.
success_notification = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='cart-link']")))
success_notification.click()

# 5. Check the "Terms of service" checkbox and click the "Checkout" button.
terms_of_service_checkbox = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//label[contains(@for,'cart'])//input[contains(@class,'form-check')]")))
terms_of_service_checkbox.click()
checkout_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='checkout-button']")))

# 6. Choose "Checkout as Guest".
guest_checkout_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//label[contains(@for,'cart'])//input[contains(@value,'guest')]")))
guest_checkout_button.click()

# 7. Fill out the full billing form (from credentials):
    - First name, last name, email (generated), address, city, country, zip code, phone.
address_input = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@id,'address')]")))
address_input.send_keys("123 Main St")

city_input = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@id,'city')]")))
city_input.send_keys("Riga")

country_select = Select(address_input)
country_id = "LV-1234"

# 8. Proceed through the following:
    - Shipping method step.
    - Payment method step.
    - Payment info step (fill in credit card details from credentials if necessary).
shipping_method_step_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='shipping-method-step-button']")))
payment_method_step_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='payment-method-step-button']")))

payment_info_step_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='payment-info-step-button']")))
credit_card_type = Select(payment_info_step_button)
credit_card_type.select_by_value("visa")

cardholder_name_input = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@id,'cardholder-name')]")))
cardholder_name_input.send_keys("Test User")

card_number_input = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@id,'card-number')]")))
card_number_input.send_keys("4111111111111111")

exp_month_input = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@id,'expiration-month')]")))
exp_month_input.send_keys("4")

exp_year_input = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@id,'expiration-year')]")))
exp_year_input.send_keys("2027")

card_code_input = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@id,'card-code')]")))
card_code_input.send_keys("123")

# 9. On the confirm step, click "Confirm" and wait for the success message.
confirm_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='confirm-button']")))

success_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'order-message')]//span[contains(@class,'text-order-message-error')]")))
self.assertEqual(success_message, "Thank you")

# Confirm that the order has been completed by checking:    - The confirmation text "Thank you" appears.
if "Thank you" not in success_message:
self.fail("Order completion message 'Thank you' was not found.")

if __name__ == "__main__":
unittest.main()