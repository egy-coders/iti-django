from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("login/", views.login_page, name="login" ),
    path("about/", views.about, name="about" ),
    path("cats/", views.cats, name="cats" ),
    path("cats/<int:cat_id>/", views.cat, name="cat"),
    path("products/", views.products, name="products"),
    path("products/<int:product_id>/", views.proudct, name='product'),
    path("add_product/", views.add_product, name="add_product"),
    path("contact/", views.contact_view, name="contact"),
    
]