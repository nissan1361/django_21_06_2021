import os, json

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product

JSON_PATH = 'mainapp/jsons'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('categories')

        ProductCategory.objects.all().delete()

        for category in categories:
            new_category = ProductCategory(**category)
            new_category.save()

        products = load_from_json('products')

        Product.objects.all().delete()
        for product in products:
            category_name = product['category']
            _category = ProductCategory.objects.get(name=category_name)
            product['category'] = _category

            new_category = Product(**product)
            new_category.save()

        super_user = ShopUser.objects.create_superuser('admin', 'example@mail.com', '123', age='30')