import pytest
import requests


class TestClass(object):
    def test_get_categories_for_store(self):
        response_check = requests.get(url='http://127.0.0.1:5000/items/?store_id=1').json()
        assert response_check == [10, 1, 2]

    def test_get_item_inventory(self):
        response_check = requests.get(url='http://127.0.0.1:5000/items/?item_name=shirt').json()
        assert response_check == [{"category": 10, "item_name": "shirt", "items": 10, "price": 100, "store": 1}]

    def test_get_median_for_category(self):
        response_check = requests.get(url='http://127.0.0.1:5000/items/?category_id=10').json()
        assert response_check == 50
