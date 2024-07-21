from django.urls import path
from .views import CategoryListView, SubCategoryListView
urlpatterns = [
    path('', CategoryListView.as_view(), name='category-list'),
    path('subcatgory', SubCategoryListView.as_view(), name='category-sub-list'),
]