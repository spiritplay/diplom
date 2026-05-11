from django.urls import path
from . import views

urlpatterns = [
    path('',views.shop,name='shop'),
    path('category/<slug:slug>/',views.category_view,name='category_view'),
    path('product/<slug:slug>/',views.product_view,name='product_view'),
    path('product/<slug:slug>/', views.product_view, name='product_view'),
    path('product/<slug:slug>/like/', views.toggle_like, name='toggle_like'),
    path('wishlist/', views.wishlist, name='wishlist'),


]