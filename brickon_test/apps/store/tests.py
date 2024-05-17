from brickon_test.config.tests import ConfigAPITest
from rest_framework import status
from .models import Product

# Create your tests here.


class ProductTestCase(ConfigAPITest):
    def setUp(self):
        self.user = self.create_user()
        self.product_path = "/store/products/"
        self.authenticate(self.user)

    def test_restaurant_create(self):
        data_request = {
            "name": "Pepsi",
            "description": "Pepsi de 1litro",
            "price": 20,
            "sku": "PEPSI0001"
        }
        response = self.client.post(f"{self.product_path}", data=data_request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_products_list(self):
        response = self.client.get(f"{self.product_path}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_restaurant_delete(self):
        self.test_restaurant_create()
        product = Product.objects.first()
        response = self.client.delete(f"{self.product_path}{product.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_restaurant_update(self):
        self.test_restaurant_create()
        product = Product.objects.first()
        data_request = {
            "name": "Pepsi editado",
            "description": "Pepsi de 1 litro editado",
            "price": 24,
            "sku": "PEPSI0002"
        }
        response = self.client.put(f"{self.product_path}{product.id}/", data=data_request)
        self.assertNotEqual(response.data["name"], product.name)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
