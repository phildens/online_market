from django.urls import path
from .views import CategoryListView, SubCategoryListView, ProductInCategoryListView, SubCategoryProductListView

urlpatterns = [
    path('', CategoryListView.as_view(), name='category-list'),
    path('subcategory/', SubCategoryListView.as_view(), name='category-sub-list'),
    path('subcategory/<int:category_id>/', SubCategoryProductListView.as_view(), name='category-sub-product-list'),
    path('<int:category_id>/', ProductInCategoryListView.as_view(), name='category-product-in-category'),
]