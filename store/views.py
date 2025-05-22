from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .forms import ContactForm, ProductForm

def index(request):
    cats = Category.objects.all()
    context = {
        'cats':cats,
        'page_title': 'Home',
    }
    return render(request, 'store/index.html', context)

def login_page(request):
    return render(request, 'store/login.html')

# def add_product(request):
#     context = {
#         'page_title': 'Add New Product',
#     }
#     return render(request, 'store/add_product.html', context)

    
def about(request):
    context = {
        'page_title':'About'
    }
    return render(request, 'store/about.html', context)


def products(request):
    products = Product.objects.all()
    context = {
        "page_title":'Products',
        'products': products
    }
    return render(request, 'store/products.html', context)

# Show single Product
def proudct(request, product_id):
    product = Product.objects.get(pk=product_id)
    context = {
        "page_title":'Products',
        'product': product
    }
    return render(request, 'store/product.html', context)

def cats(request):
    cats = Category.objects.all()
    context ={
        'cats' :cats,
        'page_title' : 'Home'
    }
    return render(request, 'store/cats.html', context)

def cat(request, cat_id):
    cat = Category.objects.get(id=cat_id)
    context ={
        'cat' :cat,
        'page_title' : 'Home'
    }
    return render(request, 'store/cat.html', context)

def contact_view(request):
    form = ContactForm(request.POST)

    if form.is_valid():
        name = form.cleaned_data['name']
        phone = form.cleaned_data['phone']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        Contact.objects.create(name= name, phone=phone, email=email, message=message)
        return HttpResponse("Form Submited!!")
    else:
        form = ContactForm()
    context = {
        'form':form
    }
    return render(request, 'store/contact.html', context)


def add_product(request):
    form = ProductForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('products')
    else:
        form = ProductForm()
    context = {
        'page_title': 'Add New Product',
        'form':form
    }
    return render(request, 'store/add_product.html', context)
