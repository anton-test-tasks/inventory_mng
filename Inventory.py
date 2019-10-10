import json
import statistics


class Inventory(object):
    """
    Inventory Management system 
    """

    data = []

    def __init__(self):
        with open('inventory.txt') as json_file:
            self.data = json.load(json_file)

    def get_categories_for_store(self, store):
        """
        Given a store id you should return all the categories ids in the inventory.
        :param store: store id
        :return: all the categories ids in the inventory
        """
        result = []

        for item in self.data:
            if item['store'] == store:
                result.append(item['category'])

        return result

    def get_item_inventory(self, item_name):
        """
        Given items name return all the items across all stores.
        :param item: item name
        :return: all the items across all stores
        """
        result = []

        for item in self.data:
            if item_name in item['item_name']:
                result.append(item)

        return result

    def get_median_for_category(self, category):
        """
        Given category id return the median of the prices for all items in the category.
        :param category: category name
        :return: the median of the prices for all items in the category
        """
        result = []

        for item in self.data:
            if item['category'] == category:
                result.append(item['price'])

        return statistics.median(result)
