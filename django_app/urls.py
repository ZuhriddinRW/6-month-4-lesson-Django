from django.urls import path
from .views import *

urlpatterns = [
    path ( '', index, name='index' ),
    path ( 'news', news, name='news' ),
    path ( 'categories', categories, name='categories' ),
    path ( 'products', products, name='products' ),
    path ( 'suppliers', suppliers, name='suppliers' ),
    path ( 'categories/<int:category_id>/', categories_with_id, name='categories_by_id' ),
    path ( 'products/<int:category_id>/', products_by_category, name='products_by_category' ),
    path ( 'add_news/', add_news, name="add_news" ),
    path ( 'add_category/', add_category, name="add_category" ),
    path ( 'add_product/', add_product, name="add_product" ),
    path ( 'add_supplier/', add_supplier, name="add_supplier" ),
    path ( 'news/delete/<int:news_id>/', delete_news, name="delete_news" ),
    path ( 'category/delete/<int:category_id>/', delete_category, name='delete_category' ),
    path ( 'product/delete/<int:product_id>/', delete_product, name='delete_product' ),
    path ( 'supplier/delete/<int:supplier_id>/', delete_supplier, name='delete_supplier' ),
    path ( 'news/update/<int:news_id>/', update_news, name='update_news' )
]