from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet, basename='product')
router.register(r'users', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls))
]




# product_list = ProductViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
#
# product_detail = ProductViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'delete': 'destroy'
# })
#
# product_highlight = ProductViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })
#
# urlpatterns = [
#     path('', views.api_root),
#     path('products/', product_list, name='product-list'),
#     path('products/<int:pk>/', product_detail, name='product-detail'),
#     path('products/<int:pk>/highlight/', product_highlight, name='product-highlight'),
#     path('users/', user_list, name='user-list'),
#     path('users/<int:pk>/', user_detail, name='user-detail')
# ]
#     #======================================
    # path('p/', views.ProductList.as_view()),
    # path('p/<int:pk>/', views.ProductDetail.as_view()),
    # path('users/', views.UserList.as_view()),
    # path('users/<int:pk>/', views.UserDetail.as_view()),
    # path('', views.api_root),
    # path('<int:pk>/highlight/', views.ProductDetail.as_view()),
    #================================
    # path('', views.api_root),
    # path('products/',
    #      views.ProductList.as_view(),
    #      name='product-list'),
    # path('products/<int:pk>/',
    #      views.ProductDetail.as_view(),
    #      name='product-detail'),
    # path('products/<int:pk>/highlight/',
    #      views.ProductHighlight.as_view(),
    #      name='product-highlight'),
    # path('users/',
    #      views.UserList.as_view(),
    #      name='user-list'),
    # path('users/<int:pk>/',
    #      views.UserDetail.as_view(),
    #      name='user-detail')

