import sys
import os
import pytest
import json
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from pages.search_page import SearchPage
from pages.cart_page import CartPage
from utils.base_test import BaseTest

# Load data from input.json
def load_test_data():
    json_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'..', 'input.json')
    with open(json_file_path, 'r') as f:
        data = json.load(f)
    return data["ecommerce_test_cases"]

class TestECommerce(BaseTest):

    @pytest.mark.parametrize("test_case", load_test_data())
    def test_search_and_cart_flow(self, test_case):
        search_page = SearchPage(self.driver)
        cart_page = CartPage(self.driver)

        search_term = test_case["search_term"]
        quantity = test_case["quantity"]

        # Step 1: Search for the product
        search_page.search_product(search_term)
        result_message = search_page.get_results_message()

        # Check if the search yielded results
        if  result_message.startswith("No results for"):
            # Validate "No results found" case
            assert result_message.startswith("No results for"), f"Expected 'No results found' message for {search_term}"
            print(f"Test Case: No results found for '{search_term}'")
        else:
            # Validate that results are found
            assert result_message == "Results found", f"Results found for '{search_term}'"
            print(f"Test Case: Results found for '{search_term}'")

            # Step 3: Add product to cart and other actions
            cart_page.add_product_to_cart(7)
            print("4th Product added to cart")
            
            # Verify the subtotal
            subtotal_label, subtotal_amount = cart_page.get_cart_subtotal()
            print(f"Subtotal: {subtotal_label}, Amount: {subtotal_amount}")
            #step 4: update quantity in the cart
            cart_page.update_quantity(quantity)
            print("Updated quantity in the cart")
            # Verify the subtotal
            subtotal_label, subtotal_amount = cart_page.get_cart_subtotal()
            print(f"Subtotal: {subtotal_label}, Amount: {subtotal_amount}")

            assert cart_page.is_cart_empty() is False, "Cart should not be empty after adding the product"
            #step 5: remove product from the cart
            cart_page.remove_product_from_cart()
            assert cart_page.is_cart_empty(), "Cart should be empty after removing the product"
