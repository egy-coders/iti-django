from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about" ),
    path("cats/", views.cats, name="cats" ),
    path("products/", views.products, name="products" ),
    path("products/<int:product_id>/", views.proudct, name='product')
]