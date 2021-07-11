from django.test import TestCase
from .core_generate_promo import get_json_promo
from json import load
import os

class TestClass(TestCase):

    def test_count_group_and_amount(self):
        path = f'checker/templates/data_promo.json'
        get_json_promo(10, 'агенства', path=path)
        get_json_promo(1, 'агенства', path=path)
        get_json_promo(42, 'avtostop', path=path)
        get_json_promo(5, '1', path=path)

        with open(path, 'r') as f:
                data = load(f)
        
        set_group = set()
        count_amount = 0

        for item in data:
            item = dict(item)
            set_group.add(item['name'])
            count_amount += len(item['promo']) 
        
        os.remove(path)
        self.assertEqual(count_amount, 58)
        self.assertEqual(len(set_group), 3)
