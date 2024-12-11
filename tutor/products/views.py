from django.contrib.auth.models import User
from rest_framework import permissions, viewsets, renderers
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Product
from .permissions import IsOwnerOrReadOnly
from .serializers import ProductSerializer, UserSerializer


# PRODUCT
# class ProductList(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#
#
# class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly,
#                           IsOwnerOrReadOnly]
# class ProductHighlight(generics.GenericAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#     def get(self, request, *args, **kwargs):
#         product = self.get_object()
#         return Response(product.highlight())
# -> ProductViewSet
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        product = self.get_object()
        return Response(product.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# USER
# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
# -> UserViewSet
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#DON'T NEED BECAUSE USE DEFAULT ROUTER
# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'users': reverse('user-list', request=request, format=format),
#         'products': reverse('product-list', request=request, format=format),
#     })
