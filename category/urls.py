from django.urls import path
from .views import CategoryListView, SubCategoryListView, product_in_subcategory, product_in_category
urlpatterns = [
    path('', CategoryListView.as_view(), name='category-list'),
    path('subcatgory/', SubCategoryListView.as_view(), name='category-sub-list'),
    path('subcatgory/<int:category_id>/', product_in_subcategory),
    path('<int:category_id>/', product_in_category),
]