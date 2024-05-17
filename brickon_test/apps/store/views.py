from django.shortcuts import render
from .models import Product
from rest_framework import mixins, viewsets, status
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from brickon_test.config.paginations import DefaultPagination
from .serializers import ProductSerializer
from .filters import ProductFilter

# Create your views here.


class ProductViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = [IsAuthenticated, ]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = ProductFilter
    pagination_class = DefaultPagination
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
