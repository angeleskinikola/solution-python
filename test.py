import unittest

import grouper
from test_utils import get_items, get_grouped_by_currency_expected, get_grouped_by_multiple_keys


class TestGrouper(unittest.TestCase):
    def test_grouper_currency_key(self):
        result = grouper.group(get_items(), ["currency"])

        expected = get_grouped_by_currency_expected()

        self.assertEqual(expected, result)

    def test_grouper_multiple_keys(self):
        result = grouper.group(get_items(), ["currency", "country", "city"])

        expected = get_grouped_by_multiple_keys()

        self.assertEqual(expected, result)
