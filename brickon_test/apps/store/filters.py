from django_filters.rest_framework import FilterSet
from .models import Product
from django_filters.rest_framework import CharFilter


class ProductFilter(FilterSet):
    name = CharFilter(field_name="name", lookup_expr="icontains")
    sku = CharFilter(field_name="sku", lookup_expr="icontains")

    class Meta:
        model = Product
        fields = [
            "name",
            "sku",
            "is_active",
        ]
