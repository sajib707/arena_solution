from django.urls import path, include
from . import views


app_name = 'bookshop'


urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.book_list, name='book_list'),
    path('add/', views.add_book, name='add_book'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('api/add_to_cart/', views.AddToCartAPIView.as_view(), name='add_to_cart_api'),
]
