from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedRelatedField(view_name='product-highlight', format='html', read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.HyperlinkedRelatedField(many=True, view_name='product-detail', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'products']