from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def add_product_to_cart(self, index):
        try:
            time.sleep(2)
            product = self.driver.find_element(By.CSS_SELECTOR, f'div[data-index="{index}"]')
            product.click()
            time.sleep(2)
            self.driver.find_element(By.ID, 'a-autoid-4-announce').click()
            time.sleep(2)
            self.driver.find_element(By.ID, "nav-cart-count").click()
            time.sleep(2)
        except Exception as e:
            print(f"An error occurred: {e}")

    def update_quantity(self, quantity):
        try:
            quantity_select = self.driver.find_element(By.NAME, "quantity")
            quantity_select.send_keys(str(quantity))
            # self.driver.find_element(By.NAME, "proceedToRetailCheckout").click()
            time.sleep(3)
        except Exception as e:
            print(f"An error occurred: {e}")



    def remove_product_from_cart(self):
        try:
            # Wait until the delete button is present
            delete_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@data-action='delete' and @value='Delete']"))
            )
            delete_button.click()
            time.sleep(5)
        except Exception as e:
            print(f"An error occurred: {e}")
    def get_cart_subtotal(self):
        try:
            time.sleep(2)
            subtotal_label = self.driver.find_element(By.ID, "sc-subtotal-label-activecart").text
            subtotal_amount = self.driver.find_element(By.ID, "sc-subtotal-amount-activecart").text
            return subtotal_label, subtotal_amount
        except NoSuchElementException:
            print("Subtotal information is not available.")
            return None, None
    def is_cart_empty(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "h2.a-size-extra-large"))
            )
            return "Your Amazon Cart is empty." in self.driver.page_source
        except NoSuchElementException:
            return False
