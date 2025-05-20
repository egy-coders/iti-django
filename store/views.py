from django.shortcuts import render
from .models import Category

def index(request):
    users = [
        {"id":1, "username":"Farid", "age":33, "salary":12000}
    ]
    context = {
        'users':users,
        'page_title': 'Home'
    }
    return render(request, 'store/index.html', context)
    
def about(request):
    context = {
        'page_title':'About'
    }
    return render(request, 'store/about.html', context)


def products(request):
    products = [
        {"id":1, "name":"Mobile", "price":320},
        {"id":2, "name":"TV", "price":380},
        {"id":3, "name":"Labtop", "price":520},
    ]
    context = {
        "page_title":'Products',
        'products': products
    }
    return render(request, 'store/products.html', context)

# Show single Product
def proudct(request, product_id):
    product = [
        {"id":1, "name":"Mobile", "price":320},
        {"id":2, "name":"TV", "price":380},
        {"id":3, "name":"Labtop", "price":520},
    ]
    context = {
        "page_title":'Products',
        'product': product[product_id - 1]
    }
    return render(request, 'store/product.html', context)

def cats(request):
    cats = Category.objects.all()
    context ={
        'cats' :cats
    }
    return render(request, 'store/cats.html', context)
